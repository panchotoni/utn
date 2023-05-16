package operaciones;

public class Aritmetica {
    //ATRIBUTOS
    int a;
    int b;

     public Aritmetica() { //ESTO ES UN CONSTRUCT
         System.out.println("Primer constructor");
     }

     public Aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
         System.out.println("Se esta ejecutando este constructor");
     }

    //METODO
    public void sumarNumero() {
        int resultado = a + b;
        System.out.println(resultado);
    }
    public int sumarConRetorno () {
        return a + b;
    }

    public int sumarConArgumentos (int a, int b) {
         this.a = a;
         this.b = b;
         return this.sumarConRetorno();
    }
}
