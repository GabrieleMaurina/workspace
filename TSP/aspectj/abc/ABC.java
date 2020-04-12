class A{
  public static void a(){
    System.out.println("AAAAAAAA");
  }
}
class B{
  public static void b(){
    A.a();
  }
}
class C{
  public static void c(){
    B.b();
  }
}

public class ABC{
  public static void main(String[] args) {
    C.c();
  }
}
