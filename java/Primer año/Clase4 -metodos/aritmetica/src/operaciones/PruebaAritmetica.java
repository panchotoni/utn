package operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica artimetica1 = new Aritmetica();
        artimetica1.a = 3;
        artimetica1.b = 7;
        miMetodo();
        artimetica1.sumarNumero();

        int resultado = artimetica1.sumarConRetorno();
        System.out.println(resultado);

        resultado = artimetica1.sumarConArgumentos(12, 26);
        System.out.println(resultado);

        System.out.println(artimetica1.a);
        System.out.println(artimetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println(aritmetica2.a);
        System.out.println(aritmetica2.b);
        Persona persona = new Persona("Francisco", "Tonidandel");
        System.out.println(persona);
        System.out.println(persona.nombre);
        System.out.println(persona.apellido);
    }

    public static void miMetodo() {
        int a = 10;
        System.out.println(a);
    }
}

class Persona {
    String nombre;
    String apellido;

    Persona(String nombre, String apellido) {
        new Imprimir().imprimir(this);

        this.nombre = nombre;
        this.apellido = apellido;
    }
}

class Imprimir {
    public Imprimir(){
        super();
    }

    public void imprimir (Persona persona) {
        System.out.println("Personda desde la clase imprimir" + persona);
        System.out.println("Impresion del objeto actual (this)"+ this);
    }


}