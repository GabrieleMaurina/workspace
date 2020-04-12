class A{
public void a(){ new B().b();}
}

class B{
  public void b(){}
}

public class ThisTarget{
  public static void main(String[] args){
    new A().a();
  }
}
