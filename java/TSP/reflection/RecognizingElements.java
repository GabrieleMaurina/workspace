import java.util.stream.Stream;
import java.util.stream.Collectors;
import java.lang.Class;
import java.security.KeyPair;

public class RecognizingElements{
  public static void main(String[] args){
    var classNames = new String[]{"java.lang.String", "java.lang.Integer", "java.lang.Double"};
    var fieldNames = new String[]{"LATIN1", "serialVersionUID", "MAX_EXPONENT"};

    Stream.of(fieldNames).flatMap(f ->
        Stream.of(classNames).
          map(c -> {
            try{return Class.forName(c);}
            catch(ClassNotFoundException e){return null;}}).
          filter(c -> c != null).
          map(c -> {
            try{return c.getDeclaredField(f);}
            catch(NoSuchFieldException | SecurityException e){return null;}
          })
    ).filter(f -> f != null).
    forEach(f -> System.out.println(f.toGenericString()));
  }
}
