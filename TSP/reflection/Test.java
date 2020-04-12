public class Test{
	public int x = 2;

	public int a(int a){
		System.out.println("Executing method A");
		return a * 2;
	}
	
	public static void main(String[] args){
		System.out.println("Starting main");
		Test t = new Test();
		t.a(3);
		int x = t.x;
		t.x = 3;
	}
}
