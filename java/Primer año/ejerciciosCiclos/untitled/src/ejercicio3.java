import java.util.Scanner;

public class ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int num = Integer.parseInt(entrada.nextLine());
        int acc = 0;
        while (num > 0) {
            acc += 1;
            System.out.println("Digite otro numero");
            num = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Has introducido " + acc + " numeros");
        System.out.println("Se termino el ciclo");
    }
}
