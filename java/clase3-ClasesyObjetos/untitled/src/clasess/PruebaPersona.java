package clasess;

public class PruebaPersona {
    public static void main(String[] args) {
        Personas persona1 = new Personas();
        persona1.nombre = "Francisco";
        persona1.apellido = "Tonidandel";
        persona1.obtenerInfo();


        Personas persona2 = new Personas();
        persona2.nombre = "Carolina";
        persona2.apellido = "Bilan";
        persona2.obtenerInfo();
    }
}
