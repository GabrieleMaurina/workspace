import java.awt.AWTException;
import java.awt.Robot;

public class MiningBot
{
	private static final int X_SCREEN = 1920;
	private static final int Y_SCREEN = 1080;
	private static final int X_CENTER = X_SCREEN / 2;
	private static final int Y_CENTER = Y_SCREEN / 2;
	
	private static Robot r;
	
	public static void main(String[] args)
	{
		try {
			r = new Robot();
		} catch (AWTException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		r.delay(5000);
		
		for(int i = 0; i < 100; i++)
		{
			r.delay(100);
			r.mouseMove(X_CENTER, Y_CENTER);
			
			/*r.delay(1000);
			r.mouseMove(X_CENTER, Y_CENTER - 200);*/
		}
	}

}
