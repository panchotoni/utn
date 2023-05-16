package test;
import dominio.*;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);

        //Modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
    }
}
