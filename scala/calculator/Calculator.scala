object Calculator{
	def main(args:Array[String]){
		val p = new CalculatorParser()
		args.foreach{filename =>
			val src = scala.io.Source.fromFile(filename)
			val input = src.mkString
			p.parseAll(p.asdf, input) match {
				case p.Success(r, _) => println(r.toString)
				case x => println(x.toString)
			}
			src.close()
		}
	}
}
