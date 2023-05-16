import java.util.Scanner;

public class ciclos {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero");
        int num = entrada.nextInt();
        while (num != 0) {
            if((num & 2) == 0) {
                System.out.println("El numero es par");
            } else {
                System.out.println("El numero es impar");
            }
            num = entrada.nextInt();
        }
        System.out.println("Se termino el ciclo");
    }
}
