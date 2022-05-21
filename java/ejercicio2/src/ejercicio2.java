import java.util.Scanner;

public class ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese el salario x hs: ");
        double salariohs = Double.parseDouble(entrada.nextLine());
        System.out.println("Digite las horas trabajadas en la semana: ");
        int hs = Integer.parseInt(entrada.nextLine());

        double salarioTotal = hs * salariohs;
        System.out.println("El salario de la semana de trabajo es = us$ " + salarioTotal);

    }
}
