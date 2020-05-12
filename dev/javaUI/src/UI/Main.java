package UI;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ChoiceBox;
import javafx.stage.Stage;

public class Main extends Application {

    private Scene ui;

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("UI.fxml"));
        primaryStage.setTitle("EdYuCator");
        Scene scene = new Scene(root, 1200, 700);  // set size!
        primaryStage.setScene(scene);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
