package PasoPorReferencia;

import  clasess.Personas;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Personas personas2 = new Personas();
        personas2.nombre = "Ester";
        System.out.println("personas2 nombre= " + personas2.nombre);
        cambiarValor(personas2);
        System.out.println("personas2 nombre = " + personas2.nombre);
    }
    
    public static void cambiarValor (Personas personas) {
        personas.nombre = "Maria";
    }
}
