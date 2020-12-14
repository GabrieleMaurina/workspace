class Foo{}
class Bar{}

public class ClassLoading{
  public static void main(String[] args){
    MyClassLoader mcl = new MyClassLoader(ClassLoader.getSystemClassLoader());

    try{
      Class myStringClass = mcl.loadClass("java.lang.String");
      String myString = (String)myStringClass.getConstructor(String.class).newInstance("asdf");
      System.out.println(myString);
      mcl.loadClass("java.lang.Integer");
      mcl.loadClass("java.lang.Double");
      mcl.loadClass("java.lang.Float");
    }
    catch(Exception e){
      e.printStackTrace();
    }
  }
}
