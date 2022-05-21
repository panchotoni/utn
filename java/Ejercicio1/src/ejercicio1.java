import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese el nomre del libro ");
        String nombre = entrada.nextLine();
        System.out.println("Digite el id ");
        int id = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro ");
        double precio = Double.parseDouble(entrada.nextLine());
        System.out.println("El envio es gratuito? ");
        boolean envio = Boolean.parseBoolean(entrada.nextLine());
        Integer num = 10;

        System.out.println(nombre+ " #"+id);
        System.out.println("El precio del libro es: $"+precio);
        System.out.println("El envio del libro es gratuito es: "+envio);

    }
}
