package view;

import javax.swing.*;
import java.awt.*;

public class Interface {

    private JFrame frame;
    private JPanel panel;
    private JTextField espacoNumero;
    private JButton botaoContar, botaoResetar;

    public Interface() {
        frame = new JFrame();
        frame.setSize(450, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);

        panel = new JPanel(new BorderLayout());
        panel.setLayout(new GridLayout(3, 1, 10, 10));
        panel.setBackground(Color.white);

        espacoNumero = new JTextField(" 0 ");
        panel.add(espacoNumero, BorderLayout.NORTH);
        espacoNumero.setEditable(false);

        botaoContar = new JButton("Contar");
        botaoResetar = new JButton("Resetar");
        panel.add(botaoContar, BorderLayout.CENTER);
        panel.add(botaoResetar, BorderLayout.SOUTH);

        estilizacaoEspacoNumero(espacoNumero);
        estilizacaoBotoes(botaoContar);
        estilizacaoBotoes(botaoResetar);

        frame.add(panel);
        frame.setVisible(true);

    }

    public JButton getBotaoContar() {
        return botaoContar;
    }

    public JButton getBotaoResetar() {
        return botaoResetar;
    }

    public JTextField getEspacoNumero() {
        return espacoNumero;
    }

    private static void estilizacaoEspacoNumero(JTextField en) {
        en.setFont(new Font("Arial", Font.BOLD, 40));
        en.setBackground(Color.LIGHT_GRAY);
        en.setHorizontalAlignment(JTextField.CENTER);
        en.setBorder(BorderFactory.createLineBorder(Color.black));
    }

    private static void estilizacaoBotoes(JButton b) {
        b.setBackground(Color.LIGHT_GRAY);

        b.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(Color.black),
                BorderFactory.createEmptyBorder(50, 50, 50, 50)
        ));

        b.setPreferredSize(new Dimension(250, 250));
    }
}