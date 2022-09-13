import javax.swing.*;

public class ejercicio3JOption {
    public static void main(String[] args) {

        int num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        int acc = 0;

        while (num > 0) {
            acc += 1;
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        }
        JOptionPane.showMessageDialog(null, "Ingreaste " + acc + " numeros");
    }
}
