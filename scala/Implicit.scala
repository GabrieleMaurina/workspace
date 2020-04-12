object Implicit{
	implicit class Wrong(x:Double){
		def + (y:Double) = Wrong(x * y)
	}

	def main(args:Array[String]){
		println(Wrong(3) + 4)
	}
}
