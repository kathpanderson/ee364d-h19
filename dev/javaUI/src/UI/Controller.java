/*
    To build jar, see
    https://www.jetbrains.com/help/idea/compiling-applications.html
    After changing code, new JAR must be generated and put into prod
    folder!
 */

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
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Date;
import java.util.LinkedHashMap;
import java.util.stream.StreamSupport;

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
    private Button generateMovieButton;

    @FXML
    private Button displayBlobButton;

    @FXML
    private TextField selectedVisualFile;

    @FXML
    private TextField blobNumber;

    @FXML
    private CheckBox launchProcessingCheckbox;

    @FXML
    private CheckBox launchVisualizerCheckbox;

    @FXML
    private AnchorPane uiParent;

    @FXML
    private TextField selectedProcessingFile;

    @FXML
    private TextField customDataPath;

    @FXML
    private CheckBox customDataPathCheckbox;

    @FXML
    private Button selectCustomDataPath;

    private FileChooser fChooser;

    private DirectoryChooser dChooser;

    private String PYTHON = "python3";

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
    private File destinationDir = null;

    // TODO visualizer and data path stuff!
    @FXML
    private void handleRunTest(ActionEvent event) {
        if (!testRunning) {
            testRunning = true; // start test

            // Alter button to stop test button
            runTestButton.setText("Stop Test");
            runTestButton.setStyle("-fx-background-color: #ff0000; -fx-text-fill: #ffffff;");

            // Get destination directory
            this.destinationDir = null;
            if (customDataPathCheckbox.isSelected()) {
                this.destinationDir = new File(customDataPath.getText());
            }
            else {
                this.destinationDir = new File(generateDefaultPath());
                // Create directory if it doesn't already exist
                this.destinationDir.mkdir();
            }

            // Run the DAQ software to collect data
            launchDAQ(this.destinationDir);
        }
        else {
            testRunning = false;  // end test

            // Kill DAQ software
            this.daqExe.destroy();

            // Run processing on data if selected
            if (launchProcessingCheckbox.isSelected()) {
                runTestButton.setText("Processing Data...");
                runTestButton.setStyle("");
                runTestButton.setDisable(true);

                // Execute processing stuff
                executeProcessing(this.destinationDir, "RawData");  // busy wait fxn call

                if (launchVisualizerCheckbox.isSelected()) {
                    String datapath = destinationDir.getAbsolutePath() + "\\ProcessedData.csv";
                    generateMovie(datapath);
                }
            }
            // Set button back to original state
            runTestButton.setText("Start Test");
            runTestButton.setDisable(false);
        }
    }

    // Stitches an array of strings back together into a single string to use as directory string
    private String stitchStrings(String[] arr) {
        String result = "";

        for (int i = 0; i < arr.length - 2; i++) {
            result += "\\" + arr[i];
        }

        return result;
    }

    @FXML
    private void handleRunProcessing(ActionEvent event) {
        String pathStr = selectedProcessingFile.getText();
        try {
            // Split file path
            String[] split = pathStr.split("\\\\");
            String filename = split[split.length-1].split("\\.")[0];
            System.out.println(filename);

            File destinationDir = new File(stitchStrings(split));

            executeProcessing(destinationDir, filename);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void launchDAQ(File destinationDir) {
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

        String destination = destinationDir.getAbsolutePath() + "\\RawData.tdms";

        // Launch DAQ executable
        try {
            String daqExePath = System.getProperty("user.dir") + "\\daq\\daq.exe";  // TODO change to correct file
            this.daqExe = new ProcessBuilder(daqExePath,param0, param1, param2, param3, destination).start();
        } catch (IOException e) {
            System.out.println("Failed to open executable");
            e.printStackTrace();
        }

    }

    private void executeProcessing(File directory, String filename) {
        try {
            String processingPath = System.getProperty("user.dir") + "\\processing\\ProcessingCaller.py";
            ProcessBuilder pb = new ProcessBuilder(
                    PYTHON,
                    processingPath,
                    directory.getAbsolutePath(),
                    filename,
                    xPixelsVal.getText(),  // x pixels
                    yPixelsVal.getText(),  // y pixels
                    directory.getAbsolutePath(),  // path to save created files
                    "ProcessedData",  // name for created files
                    "0",  // test being ran (0=current, 1=photodetector) TODO: See Processing future plans!
                    tipCurrentVal.getText(),  // tested noise current
                    "10",  // expected SNR of current  // TODO: See Processing future plans!
                    photo1Val.getText(),  // tested noise photodetector 1
                    "10",  // expected SNR of photodetector 1
                    photo2Val.getText(),  // tested noise photodetector 2
                    "10"  // expected SNR of photodetector 2
            );
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

    @FXML
    private void handleSelectVisualFile(ActionEvent e) {
        File file = selectFile();
        selectedVisualFile.setText(file.getAbsolutePath());
    }

    @FXML
    private void handleDisplayBlob(ActionEvent e) {
        try {
            String script = System.getProperty("user.dir") + "\\visualization\\visualizing_cluster.py";  // TODO change to correct file

            ProcessBuilder pb = new ProcessBuilder(
                    PYTHON,  // TODO may need to fix for lab computer!
                    script,
                    selectedVisualFile.getText(),
                    blobNumber.getText()
            );
            Process processing = pb.start();

            int exitCode = processing.waitFor();  // wait for processing to end
            System.out.println("Processing exited with code " + exitCode);
        } catch (IOException exception) {
            exception.printStackTrace();
        } catch (InterruptedException exception) {
            exception.printStackTrace();
        }
    }

    @FXML
    private void handleGenerateMovie(ActionEvent e) {
        generateMovie(selectedVisualFile.getText());
    }

    private void generateMovie(String csvFile) {
        try {
            // Create mp4 file name!
            String[] split = csvFile.split("\\\\");  // get csv file
            String movieName = split[split.length-1].split("\\.")[0] + ".mp4";  // replace .csv with .mp4

            String script = System.getProperty("user.dir") + "\\visualization\\visualizing_movie.py";  // TODO change to correct file

            ProcessBuilder pb = new ProcessBuilder(
                    PYTHON,  // TODO may need to fix for lab computer!
                    script,
                    csvFile,
                    movieName
            );
            Process processing = pb.start();

            int exitCode = processing.waitFor();  // wait for processing to end
            System.out.println("Processing exited with code " + exitCode);
        } catch (IOException exception) {
            exception.printStackTrace();
        } catch (InterruptedException exception) {
            exception.printStackTrace();
        }
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

    private String generateDefaultPath() {
        String path = System.getProperty("user.dir") + "\\data";

        Date now = new Date();
        path += "\\" + now.getTime();

        return path;
    }
}
