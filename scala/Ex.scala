object Ex{
	class Editor(var s:String = "Default empty line", var c:Int = 0){
		override def toString() = s + "\n" + (for(i <- 0 until c) yield " ").mkString("") + "="
	}

	def main(args:Array[String]){
		val e = new Editor("Because you are mine, I walk the line", 0)
		println(e)
	}
}
