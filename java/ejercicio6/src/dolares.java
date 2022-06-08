import java.util.Scanner;

public class dolares {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Cuanto dolares tenes guillermo?: ");
        int dolaresG = Integer.parseInt(entrada.nextLine());
        
        int dolaresL = dolaresG/2;
        
        int dolaresT = dolaresG + dolaresL;
        
        int dolaresJ = dolaresT/2;
        
        int dolaresTotales = dolaresG + dolaresJ + dolaresL;
        System.out.println("dolaresTotales = " + dolaresTotales);
        


    }
}
