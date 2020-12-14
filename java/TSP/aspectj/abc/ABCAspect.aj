public aspect ABCAspect{
  pointcut blockBA():
    execution(* A.*(..)) &&
    cflow(call(* B.*(..)));

  before(): blockBA(){
    for(StackTraceElement e : new Throwable().getStackTrace()){
      if(e.getClassName() == "C") break;
      else if(e.getClassName() == "B") throw new RuntimeException("Cannot invoke b->a.");
    }
  }
}
