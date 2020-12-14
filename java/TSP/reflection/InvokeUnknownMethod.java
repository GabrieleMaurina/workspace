import java.lang.Class;
import java.lang.reflect.Method;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.List;
import java.util.ArrayList;

class Calculator{
	public int add(int a, int b) { return a + b; }
	public int mul(int a, int b) { return a * b; }
	public double div(double a, double b) { return a / b; }
	public double neg(double a) { return -a; }
}

public class InvokeUnknownMethod{
	public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException{ 
		Class<?> clazz = Class.forName(args[0]);
		Constructor<?> constructor = clazz.getDeclaredConstructor();
		Object object = constructor.newInstance();
		List<Class<?>> argsClasses = new ArrayList<Class<?>>();
		List<Object> argsValues = new ArrayList<Object>();
		for(int i = 2; i < args.length; i++){
			try{
				argsValues.add(Integer.parseInt(args[i]));
				argsClasses.add(int.class);
			}
			catch(NumberFormatException e){
				argsValues.add(Double.parseDouble(args[i]));
				argsClasses.add(double.class);
			}
		}
		Method method = clazz.getDeclaredMethod(args[1], argsClasses.toArray(new Class<?>[argsClasses.size()]));
		System.out.println(method.invoke(object, argsValues.toArray()));
	}
}