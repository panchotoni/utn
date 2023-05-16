import javax.swing.*;

public class Ejercicio8Factorial {
    public static void main(String[] args) {
        long factorial = 1;
        int num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));

        for(int i = 1; i<=num; i++) {
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, "El factorial es "+ factorial);
    }
}

