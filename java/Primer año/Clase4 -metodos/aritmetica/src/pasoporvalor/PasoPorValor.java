package pasoporvalor;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        cambioValor(valorX);
        System.out.println("valorX = " + valorX);
    }

    public static void cambioValor(int arg) {
        System.out.println("arg = " + arg);
        arg = 15;
        System.out.println("arg = " + arg);
    }
}
