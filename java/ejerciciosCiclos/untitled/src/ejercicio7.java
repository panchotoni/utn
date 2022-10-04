import javax.swing.*;

public class ejercicio7 {
    public static void main(String[] args) {

        float num = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        float acc = 0;
        float resultado = 0;
        float suma = 0;

        while (num >= 0) {
            suma += num;
            acc++;
            System.out.println("Digite otro numero: ");
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }

        resultado = suma / acc;
        JOptionPane.showMessageDialog(null, "El promedio es: " + resultado);




    }
}
