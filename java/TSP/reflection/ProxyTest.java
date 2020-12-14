import java.util.Date;
import java.lang.reflect.Method;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

interface ITestingFields{
  void setAnswer(int a);
  String message();
}

class TestingFields implements ITestingFields{
  private Double d[];
  private Date dd;
  private int the_answer = 42;
  public TestingFields(int n, double val) {
    dd = new Date();
    d = new Double[n];
    for(int i=0; i<n; i++) d[i] = i*val;
  }
  public void setAnswer(int a) {the_answer = a;}
  public String message() {return "The answer is "+the_answer;}
}

class StatusHandler implements InvocationHandler{
  Object base;
  StatusHandler(Object base){
    this.base = base;
  }
  private static void printStatus(Object obj){
    System.out.println(obj.getClass().toGenericString());
    Field[] fields = obj.getClass().getDeclaredFields();
    for(var f : fields){
      f.setAccessible(true);
      try{
        System.out.println("\t" + f.toGenericString() + "   " + f.get(obj));
      }
      catch(Exception e){
        e.printStackTrace();
      }
    }
  }
  public Object invoke(Object proxy, Method method, Object[] args){
    try{
      System.out.println("Status before " + method.toGenericString());
      printStatus(base);
      Object toRtn = method.invoke(base, args);
      System.out.println("Status after");
      printStatus(base);
      return toRtn;
    }
    catch(Exception e){
      e.printStackTrace();
      return null;
    }
  }
}

public class ProxyTest{
  public static void main(String[] args) {
    TestingFields tf = new TestingFields(5, 3.14);
    ITestingFields sh_tf = (ITestingFields) Proxy.newProxyInstance(
      tf.getClass().getClassLoader(), tf.getClass().getInterfaces(), new StatusHandler(tf));
    sh_tf.setAnswer(75);
    System.out.println("Answer set to 75");
    System.out.println(sh_tf.message());
  }
}
