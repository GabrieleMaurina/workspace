import java.lang.instrument.Instrumentation;

final public class Premain{
  public static void premain(String args, Instrumentation inst){
    System.out.println("Premain");
  }

  public static void main(String[] args) {
    System.out.println("Main");
  }
}
