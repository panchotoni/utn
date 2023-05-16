import java.util.Scanner;

public class calificaciones {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite la primer clasificacion: ");
        double clasi1 = Double.parseDouble(entrada.nextLine());
        System.out.println("Digite la 2 clasificacion: ");
        double clasi2= Double.parseDouble(entrada.nextLine());
        System.out.println("Digite la 3 clasificacion: ");
        double clasi3 = Double.parseDouble(entrada.nextLine());
        
        double SumaTotal = (clasi1 + clasi2 + clasi3);
        System.out.println("SumaTotal = " + SumaTotal);


    }
}
