public class MyClassLoader extends ClassLoader{
  private static int tot = 0;
  public MyClassLoader(ClassLoader parent) { super(parent); }
  @Override
  public Class<?> loadClass(String name) throws ClassNotFoundException{
    System.out.println("Loading Class - ’" + name + "’ " + ++tot);
    return super.loadClass(name);
  }
}
