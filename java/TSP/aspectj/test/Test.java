import java.lang.Math;

public class Test{
  public Test(String c){
    System.out.println(c);
  }

  public int testMethod(int a, char b){
    System.out.println("testMethod " + b);
    return a * 2;
  }

  public void cflowMethod(){this.a();}

  public void a(){this.b();}

  public void b(){System.out.println("method b");}

  public double function(double a){
    return Math.pow(a, a);
  }

  public static void main(String[] args){
    Test t = new Test("asdf");
    System.out.println(t.testMethod(2, 'c'));
    t.cflowMethod();
    System.out.println(t.function(2.0));
  }
}
