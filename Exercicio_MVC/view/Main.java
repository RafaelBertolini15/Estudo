package app;

import controller.Controlador;
import model.Modelao;
import view.Interface;

public class Main {
    public static void main(String[] args) {
        Modelao model = new Modelao();
        Interface view = new Interface();
        new Controlador(view, model);
    }
}