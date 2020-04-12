import java.lang.Class;
import java.lang.reflect.Method;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.ElementType;
import java.util.Set;
import java.util.LinkedHashSet;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface Edge{
  String clazz();
  String method();
}
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface Vertex{
  Edge[] value();
}

class A{
  public B b;
  public C c;
  @Vertex({
    @Edge(clazz="B", method="asdf"),
    @Edge(clazz="C", method="asdf")
  })
  public void asdf(){
    b.asdf();
    c.asdf();
  }
}
class B{
  @Vertex({})
  public void asdf(){}
}
class C{
  public B b;
  @Vertex({
    @Edge(clazz="B", method="asdf")
  })
  public void asdf(){
    b.asdf();
  }
}
public class ControlFlowGraph{
  public static void main(String[] args) {
    runCFG("A", "asdf", new LinkedHashSet<Vertex>(), 0);
  }
  public static void runCFG(String clazz, String method, Set<Vertex> prev, int depth){
    try{
      Class c = Class.forName(clazz);
      Method m = c.getDeclaredMethod(method);
      Vertex v = m.getAnnotation(Vertex.class);
      String space = "";
      for(int i = 0; i < depth; i++) space += "\t";
      System.out.println(space + c.getName() + " " + m.getName());
      if(!prev.contains(v)){
        prev.add(v);
        for(var e : v.value()){
          runCFG(e.clazz(), e.method(), prev, depth+1);
        }
      }
    }
    catch(Exception e){}
  }
}
