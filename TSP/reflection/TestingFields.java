import java.util.Date;
import java.lang.reflect.Field;

public class TestingFields {
	private Double d[];
	private Date dd;
	public static final int i = 42;
	protected static String s = "testing ...";
	public TestingFields(int n, double val) {
		dd = new Date();
		d = new Double[n];
		for(int i=0; i<n; i++) d[i] = i*val;
	}
	public static void main(String[] args) throws IllegalAccessException, NoSuchFieldException{
		TestingFields tf = new TestingFields(7, 3.14);
		status(tf);
		Field s = tf.getClass().getDeclaredField("s");
		s.setAccessible(true);
		s.set(tf, "Passed!!!");
		status(tf);
	}
	public static void status(Object obj) throws IllegalAccessException, NoSuchFieldException{
		Field[] fields = obj.getClass().getDeclaredFields();
		
		for(var f : fields){
			f.setAccessible(true);
			System.out.println(f.toGenericString() + " = " + f.get(obj));
		}
	}
}