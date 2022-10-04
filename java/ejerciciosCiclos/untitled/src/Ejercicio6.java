import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");

        int num = entrada.nextInt();
        int acc= 0;

        while (num != 0) {
            acc += num;
            System.out.println("Digite otro numero");
            num = entrada.nextInt();
        }

        System.out.println("Se acabo el ciclo, la suma es de: " + acc);

    }
}
