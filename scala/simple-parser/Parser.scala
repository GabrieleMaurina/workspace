object Parser{
	def main(args:Array[String]){
		val p = new BetterParser()
		args.foreach{filename =>
			val src = scala.io.Source.fromFile(filename)
			val input = src.mkString
			p.parseAll(p.expr, input) match {
				case p.Success(r, _) => println(r)
				case x => println(x.toString)
			}
			src.close()
		}
	}
}
