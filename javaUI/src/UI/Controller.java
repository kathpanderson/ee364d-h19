package UI;

import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.stage.DirectoryChooser;
import javafx.stage.FileChooser;

import javax.swing.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedHashMap;

public class Controller {
    // References to FXML elements of interest
    @FXML
    private CheckBox ampEnabled;

    @FXML
    private ChoiceBox ampInputRange;

    @FXML
    private TextField photo1Val;

    @FXML
    private TextField photo2Val;

    @FXML
    private TextField tipCurrentVal;

    @FXML
    private TextField tipBiasVal;

    @FXML
    private TextField xPixelsVal;

    @FXML
    private TextField yPixelsVal;

    @FXML
    private TextField daqSamplingRateVal;

    @FXML
    private ChoiceBox daqSamplingRateUnit;

    @FXML
    private Button runTestButton;

    @FXML
    private Button runProcessingButton;

    @FXML
    private Button runVisualizerButton;

    @FXML
    private CheckBox launchProcessingCheckbox;

    @FXML
    private CheckBox launchVisualizerCheckbox;

    @FXML
    private AnchorPane uiParent;

    @FXML
    private Label selectedProcessingFile;

    @FXML
    private TextArea customDataPath;

    @FXML
    private CheckBox customDataPathCheckbox;

    @FXML
    private Button selectCustomDataPath;

    private FileChooser fChooser;

    private DirectoryChooser dChooser;

    // Maps text in the pre amp current range selector to a value
    // to pass to the DAQ for data collection.
    private LinkedHashMap<String, String> ampInputCurrentOptions;
    private String[] inputCurrentText = {
        "0.1mA to 10mA", // 1mA
        "10uA to 2mA",  // 100uA
        "1uA to 200uA",  // 10uA
        "100nA to 20uA",  // 1uA
        "10nA to 2uA",  // 100 nA
        "1nA to 200nA",  // 10nA
        "100pA to 20nA",   // 1nA
        "10pA to 2nA",  // 100pA
        "10pA to 200pA"  // 10pA
    };
    private String[] inputCurrentVals = {
        "+0   +0   +0   +0",
        "+0   +0   +255 +0",
        "+0   +255 +0   +0",
        "+0   +255 +255 +0",
        "+255 +0   +0   +0",
        "+255 +0   +0   +255",
        "+255 +0   +255 +255",
        "+255 +255 +0   +255",
        "+255 +255 +255 +255"
    };

    private Process daqExe;

    final String DEFAULT_DAQ_PATH = "";  // FIXME

    @FXML
    private void initialize() {
        // Initialize file and directory choosers
        fChooser = new FileChooser();
        dChooser = new DirectoryChooser();

        // Populate map to hold all DAQ input current range options
        this.ampInputCurrentOptions = new LinkedHashMap<String, String>();
        for (int i = 0; i < inputCurrentVals.length; i++) {
            ampInputCurrentOptions.put(inputCurrentText[i], inputCurrentVals[i]);
        }

        // Populate choice boxes for pre amp input current range and
        // DAQ sampling rate units
        ampInputRange.setItems(FXCollections.observableArrayList(
                inputCurrentText
        ));
        ampInputRange.setValue("0.1mA to 10mA");

        daqSamplingRateUnit.setItems(FXCollections.observableArrayList(
            "Hz", "kHz", "MHz", "GHz"
        ));
        daqSamplingRateUnit.setValue("kHz");

        // Set default values for check boxes
        launchProcessingCheckbox.setSelected(true);
        launchVisualizerCheckbox.setSelected(true);

        // Disable custom data path field
        // customDataPath.setDisable(true);
    }

    // Keeps track if a test is in progress or not.
    private boolean testRunning = false;

    @FXML
    private void handleRunTest(ActionEvent event) {
        if (!testRunning) {
            testRunning = true; // start test

            // Alter button to stop test button
            runTestButton.setText("Stop Test");
            runTestButton.setStyle("-fx-background-color: #ff0000; -fx-text-fill: #ffffff;");

            // Run the DAQ software to collect data
            launchDAQ();
        }
        else {
            testRunning = false;  // end test

            // Kill DAQ software
            this.daqExe.destroy();

            // Get data's destination path
            File destinationDir = null;
            customDataPathCheckbox.setSelected(true);  // FIXME for debugging!
            if (customDataPathCheckbox.isSelected()) {
                destinationDir = new File(customDataPath.getText());
            }
            else {
                // TODO figure out where default data paths should go!
            }

            // Move raw data to destination
            try {
                Files.move(
                        Paths.get(DEFAULT_DAQ_PATH),
                        Paths.get(destinationDir.getAbsolutePath() + "")
                );
            } catch (IOException e) {
                System.out.println("Failed to copy data to destination");
                e.printStackTrace();
            }

            // Run processing on data if selected
            if (launchProcessingCheckbox.isSelected()) {
                runTestButton.setText("Processing Data...");
                runTestButton.setStyle("");
                runTestButton.setDisable(true);

                // Execute processing stuff
                executeProcessing();

                // TODO add visualizer launch stuff
                if (launchVisualizerCheckbox.isSelected()) {
                    String datapath = destinationDir.getAbsolutePath() + "";  // FIXME
                    File data = new File(datapath);
                    launchVisualizer(data);
                }

            }

            // Set button back to original state
            runTestButton.setText("Start Test");
            runTestButton.setDisable(false);
        }
    }

    @FXML
    private void handleRunProcessing(ActionEvent event) {
        executeProcessing();
    }

    @FXML
    private void handleVisualizerLaunch(ActionEvent event) {
        File toDisplay = selectFile();
        launchVisualizer(toDisplay);
    }

    private void launchDAQ() {
        // Get params string to pass to Labview executable
        String params[];
        String param0, param1, param2, param3;
        if (ampEnabled.isSelected()) {
            String selectedVal = (String) ampInputRange.getValue();
            params = ampInputCurrentOptions.get(selectedVal).split(" ");
        }
        else {
            params = "+0 +0 +0 +0".split(" ");  // amp disabled
        }

        // Split params into individual vars
        param0 = params[0];
        param1 = params[1];
        param2 = params[2];
        param3 = params[3];

        // Launch DAQ executable
        try {
            String daqExePath = System.getProperty("user.dir") + "\\DAQ\\Application.exe";  // TODO change to correct file
            this.daqExe = new ProcessBuilder(daqExePath,param0, param1, param2, param3).start();
        } catch (IOException e) {
            System.out.println("Failed to open executable");
            e.printStackTrace();
        }

    }

    // TODO: Add parameters!
    private void executeProcessing() {
        try {
            String processingPath = System.getProperty("user.dir") + "\\processing\\main.py";  // TODO change to correct file
            ProcessBuilder pb = new ProcessBuilder("python", "-u", processingPath, "main");
            Process processing = pb.start();

            int exitCode = processing.waitFor();  // wait for processing to end
            System.out.println("Processing exited with code " + exitCode);

        } catch(IOException e) {
            System.out.println("Failed to open processing software");
            e.printStackTrace();
        } catch (InterruptedException e) {
            System.out.println("Interrupted exception");
            e.printStackTrace();
        }
    }

    // TODO: Everything
    private void launchVisualizer(File dataFile) {
        System.out.println(dataFile.getAbsolutePath());
    }

    @FXML
    private void handleSelectProcessFile(ActionEvent e) {
        File selected = selectFile();
        selectedProcessingFile.setText(selected.getAbsolutePath());
    }

    @FXML
    private void handleSelectCustomDataPath(ActionEvent e) {
        File destination = selectDirectory();
        customDataPath.setText(destination.getAbsolutePath());
    }

    private File selectFile() {
        return fChooser.showOpenDialog(uiParent.getScene().getWindow());
    }

    private File selectDirectory() {
        return dChooser.showDialog(uiParent.getScene().getWindow());
    }
}
