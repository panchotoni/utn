import  javax.swing.JOptionPane;
public class cicloss {
    public static void main(String[] args) {

        //EJERCICIO 1
        /*
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));

        while(numero >= 0){
            int cuadrado = (int)Math.pow(numero,2);
            System.out.println("El " + numero + " elevado al cuadrado es " + cuadrado);
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        }
        System.out.println("Se finalizo el ciclo while");







        */
        //EJERCICIO 2

        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (numero != 0) {
            if (numero > 0) {
                System.out.println("El numero es positivo");
            } else {
                System.out.println("El numero es negativo");
            }

            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));

        }
        System.out.println("Termino el ciclo");
    }
}
