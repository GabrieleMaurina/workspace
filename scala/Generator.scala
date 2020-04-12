object Generator{
	def p[T](v:T){
		Console.println(v)
	}
	def main(args:Array[String]){
		p(for(x <- List.range(0, 10) if x%2 == 0) yield x)
	}
}
