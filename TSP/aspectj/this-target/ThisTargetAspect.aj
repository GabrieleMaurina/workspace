public aspect ThisTargetAspect{
  pointcut test(Object thi, Object tar):
    call(* B.b()) &&
    this(thi) &&
    target(tar);

  before(Object thi, Object tar): test(thi, tar){
    System.out.println(thisJoinPoint +" " + thi.getClass() + " " + tar.getClass());
  }
}
