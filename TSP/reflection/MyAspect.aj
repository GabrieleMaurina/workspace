public aspect MyAspect{
	pointcut callA(int v):
		args(v) &&
		call(int Test.a(int));

	before(int v): callA(v){
		System.out.println("Before method A call: " + v);
	}

	after(int v) returning(int v1): callA(v){
		System.out.println("After method A call: " + v + " " + v1);
	}

	pointcut executionA(int v):
		args(v) &&
		execution(int Test.a(int));

	before(int v): executionA(v){
		System.out.println("Before method A exectution: " + v);
	}

	after(int v) returning(int v1): executionA(v){
		System.out.println("After method A exectution: " + v + " " + v1);
	}

	pointcut getX():
		get(int Test.x);

	before(): getX(){
		System.out.println("Before getting X");
	}

	after() returning(int v): getX(){
		System.out.println("After getting X: " + v);
	}

	pointcut setX(int v):
		args(v) &&
		set(int Test.x);

	before(int v): setX(v){
		System.out.println("Before setting X: " + v);
	}

	after(int v): setX(v){
		System.out.println("After setting X: " + v);
	}
}
