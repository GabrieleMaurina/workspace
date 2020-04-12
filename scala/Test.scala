object Test{
	def test(x:Int)(y:Int):Int = x * y

	def test1(x:Int) = x + 1

	def test2 = {println("test2"); 2}

	implicit class Times(n:Int){
		def times[T](f: => T) = for(i <- 0 until n) f
	}

	def main(args:Array[String]){
		println(test(3)(2))
		val a: (Int)=>Int = test(4)
		println(a(5))
		println(test1(2))
		println(test2)

		4 times println("Hello")
	}
}
