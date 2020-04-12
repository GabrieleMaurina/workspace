import java.lang.Class;
import java.lang.reflect.Method;

public class DumpMethods{
	public static void main(String[] arg) throws ClassNotFoundException{
		Method[] methods = Class.forName(arg[0]).getDeclaredMethods();
		for(Method m : methods){
			System.out.println(m.getName());
		}
	}
}