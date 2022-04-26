import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");

        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo";
        System.out.println(miVariableCadena);

        var usuario = "Pancho";
        var apellido = "Toni";
        var union = (usuario + " " + apellido);
        System.out.println(union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));

        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre); //SALTO DE LINEA
        System.out.println("Tabulador: \t" + nombre); //TABULADOR PARA MOVER EL TEXTO
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroceso: \b" + nombre); //Retroceso, es decir quitar un espacio hacia atras o una caracter que este detras
        System.out.println("Comillas simples: '" + nombre + "'");
        System.out.println("Comillas dobles: \""+ nombre+"\"");

        //Clase Scanner: SE USA PARA GUARDAR LA ENTRADA DE DATOS EN LA VARIABLE QUE ASIGNEMOS
        Scanner entrada = new Scanner(System.in);
        System.out.println("\nDigite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("Usiario2 = "+ usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+ titulo2 +" "+ usuario2);
    }
}
