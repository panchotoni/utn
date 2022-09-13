import javax.swing.*;
import java.util.Scanner;

public class ejercicio2 {
    public static void main(String[] args) {
        int numer = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));

        while (numer != 0) {
            if((numer & 2) == 0) {
                JOptionPane.showMessageDialog(null, "El numero es par");
            } else {
                JOptionPane.showMessageDialog(null, "El numero es impar");
            }
            numer = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        }
        JOptionPane.showMessageDialog(null, "El ciclo se termino");
    }
}
