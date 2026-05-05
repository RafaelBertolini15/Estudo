package model;

public class Modelao {

    private int contador = 0;

    public void somar (){
        contador++;
    }

    public void resetar (){
        contador = 0;
    }

    public int getContador() {
        return contador;
    }
}
