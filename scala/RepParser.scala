import scala.util.parsing.combinator._

object RepParser{
	class RepParser extends JavaTokenParsers{
		def list = ele ~ rep(ele) ^^ {case e ~ eles => eles.foldLeft(e){_+_}}
		def ele = """[a-zA-Z0-9]+""".r
		def num = floatingPointNumber ^^ {_.toDouble}
	}
	def main(args:Array[String]){
		val p = new RepParser()
		for(file <- args){
			val src = scala.io.Source.fromFile(file)
			val input = src.mkString
			p.parseAll(p.list, input) match {
				case p.Success(r, _) => println(r)
				case x => println("asdf%%%%%%%%%%%%%%%%%%%%%%%" + x.toString)
			}
			src.close()
		}
	}
}
