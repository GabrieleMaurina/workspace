public aspect MyAspect{
  pointcut mainPointcut(): execution(public static void Main.main(String []));

  after() returning: mainPointcut(){
    System.out.println("Hello universe!");
  }
}
