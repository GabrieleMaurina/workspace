import scala.util.parsing.combinator._
object Primary{
	class Primary extends JavaTokenParsers{
		def all = list ~ res ^^ {case l ~ r => l.sum == r}
		def list = num ~ exp ^^ {case n1 ~ (n2, op) => n1 op n2}
		def num = wholeNumber ^^ {_.toInt}
		def exp = sep ~ num
		def sep = plus | minus
		def plus = "+"
		def minus = "-"
		def res = "=" ~> """-+""".r ~> num ^^ {_.toInt}
	}
	def main(args:Array[String]){
		val p = new Primary()
		val src = scala.io.Source.fromFile(args(0))
		val input = src.mkString
		src.close()
		p.parseAll(p.all, input) match{
			case p.Success(r,_) => println(r)
			case x => println(x)
		}
	}
}
