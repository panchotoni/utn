
import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
       /* System.out.println("Hola Mundo");

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

        */

        //Inferencia de tipos var y tipos primitivos

       /*
        var numEntero = 20;
        System.out.println("Numentero = " + numEntero);

        var numfloat = 20.0F;
        System.out.println("numfloat = " + numfloat);
        
        var numDoble = 15.0;
        System.out.println("numDoble = " + numDoble);
        */

        /*
        //tipos primitivos char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        char varCaracter = 36;
        System.out.println("varCaracter = " + varCaracter);
         */
        /*
        boolean varBool = false;
        System.out.println("varBool = " + varBool);
        if (varBool) {
            System.out.println("La bandera es verde");
        }
        else {
            System.out.println("la bandera es roja");
        }

        var edad = 18;
        //var adulto = edad >=18;
        if (edad >=18) {
            System.out.println("El es mayor de edad");
        }
        else {
            System.out.println("Eres menor de edad");
        }
        */

       /* var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        //INTEGER.PARSEINT se utiliZA PARA Invertir un string a un tipo entero INT
        
        var valorPi = Double.parseDouble("3.1416");
        System.out.println("valorPi = " + valorPi);

        //PEDIR UN VALOR
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad: ");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);

       */


//        var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//
//        var fraseChar = "Programadores".charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//
//        System.out.println("Digite un caracter");
//        var entrada = new Scanner(System.in);
//        fraseChar = entrada.nextLine().charAt(12);
//        System.out.println("fraseChar = " + fraseChar);


/*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el nomre del libro ");
        String nombre = entrada.nextLine();
        System.out.println("Digite el id ");
        int id = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro ");
        double precio = Double.parseDouble(entrada.nextLine());
        System.out.println("El envio es gratuito? ");
        boolean envio = Boolean.parseBoolean(entrada.nextLine());

        System.out.println(nombre+ " #"+id);
        System.out.println("El precio del libro es: $"+precio);
        System.out.println("El envio del libro es gratuito es: "+envio);



        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion suma = " + solucion);

        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);

        solucion = num1 * num2;
        System.out.println("solucion multi = " + solucion);

        solucion = num1/num2;
        System.out.println("solucion division = " + solucion);;

        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 division = " + solucion2);

        solucion = num1 % num2; //GUARDA EL RESIDUO DE LA DIVISION
        System.out.println("solucion residuo = " + solucion);

        if (num2 % 2 == 0)
            System.out.println("es un numero par");
        else
            System.out.println("Es un numero impar");

 */
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);

        varNum1 += 1; //Es lo mismo que varNum1 = varNum1 +1;
        System.out.println("varNum1 + = " + varNum1);

        varNum2 -= 1;
        System.out.println("varNum2  - = " + varNum2);

        varNum2 *= 10;
        System.out.println("varNum2 * = " + varNum2);

        varNum2 /= 4;
        System.out.println("varNum2 / = " + varNum2);

        varNum2 %= 6;
        System.out.println("varNum2 % = " + varNum2);






    }
}
