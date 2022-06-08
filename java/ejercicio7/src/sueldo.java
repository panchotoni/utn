import java.util.Scanner;

public class sueldo {
    public static void main(String[] args) {
        final double sueldoFijo = 1000;
        double comision = 150;

        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite cuantos carros vendio");
        double carrosV = Double.parseDouble(entrada.nextLine());
        double ComisionCarros = carrosV * comision;

        System.out.println("Digite el monto total de los carros que vendio");
        double MontoTotalC = Double.parseDouble(entrada.nextLine());
        
        double comisionInd = (5*MontoTotalC)/100;
        
        double salario = sueldoFijo + ComisionCarros + comisionInd;
        System.out.println("salario = " + salario);

    }
}
