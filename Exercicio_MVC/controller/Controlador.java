package controller;

import view.Interface;
import model.Modelao;

public class Controlador {

    private Interface view;
    private Modelao model;

    public Controlador(Interface view, Modelao model) {
        this.view = view;
        this.model = model;

        configuradorDeEventos();
    }


    private void configuradorDeEventos() {

    view.getBotaoContar().addActionListener(e -> {
        model.somar();
        atualizaContador();
    });

    view.getBotaoResetar().addActionListener(e -> {
        model.resetar();
        atualizaContador();
    });

    }

    private void atualizaContador(){
        view.getEspacoNumero().
                setText(String.valueOf(model.getContador()));
    }
}
