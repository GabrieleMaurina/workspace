public aspect TestAspect{
  /*pointcut testPointcut(Test t, int a, char b):
    target(t) &&
    args(a, b) &&
    (call(int Test.testMethod(int, char)) ||
    execution(int Test.testMethod(int, char)));

  after(Test t, int a, char b) returning(int result): testPointcut(t, a, b){
    System.out.println("after returning testMethod " + t + " " + a + " " + b + " " + result);
  }

  before(Test t, int a, char b): testPointcut(t, a, b){
    System.out.println("before testMethod " + t + " " + a + " " + b);
  }

  int around(Test t, int a, char b): testPointcut(t, a, b){
    System.out.println("around before testMethod " + t + " " + a + " " + b);
    int result = proceed(t, a, b);
    System.out.println("around after testMethod " + t + " " + a + " " + b);
    return result * 5;
  }*/

  /*pointcut cflowPointcut():
    cflowbelow(call(* Test.cflowMethod())) && !within(TestAspect);

  before(): cflowPointcut(){
    System.out.println(thisJoinPoint);
  }*/

  pointcut doubleFunction(double d): args(d) && call(double *(double));

  double around(double d): doubleFunction(d){
    return proceed(proceed(d));
  }
}
