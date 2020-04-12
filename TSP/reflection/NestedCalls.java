import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Proxy;

class NestedCallsHandler implements InvocationHandler{
  public Object base;
  private int depth = 0;
  public NestedCallsHandler(Object base){
    this.base = base;
  }
  public Object invoke(Object proxy, Method method, Object[] args){
    try{
      Object toRtn = null;
      method.setAccessible(true);
      for(int i = 0; i < depth; i++) System.out.print("\t");
      System.out.println(new Throwable().getStackTrace()[2].getMethodName());
      depth++;
      toRtn = method.invoke(base, args);
      depth--;
      return toRtn;
    }
    catch(IllegalAccessException | InvocationTargetException e){
      return null;
    }
  }
}

interface INestedCalls{
  int a();
  int b(int a);
  int c(int a);
}

interface IExtendedNestedCalls{
  int callA();
  int callB(int a);
  int callC(int a);
}

class ExtendedNestedCalls extends NestedCalls implements INestedCalls,IExtendedNestedCalls{
  public IExtendedNestedCalls proxy;
  public int a() {return proxy.callA();}
  public int b(int a) {return proxy.callB(a);}
  public int c(int a) {return proxy.callC(a);}
  public int callA() {return super.a();}
  public int callB(int a) {return super.b(a);}
  public int callC(int a) {return super.c(a);}
}

public class NestedCalls{
  private int i = 0;
  public int a() {return b(i++); }
  public int b(int a) {return (i<3)?c(b(a())):1;}
  public int c(int a) {return --a;}
  public static void main(String[] args) {
    var nc = (INestedCalls)Proxy.newProxyInstance(ExtendedNestedCalls.class.getClassLoader(),
                                                          ExtendedNestedCalls.class.getInterfaces(),
                                                          new NestedCallsHandler(new ExtendedNestedCalls()));
    ((ExtendedNestedCalls)((NestedCallsHandler)Proxy.getInvocationHandler(nc)).base).proxy = (IExtendedNestedCalls)nc;
    nc.a();
  }
}
