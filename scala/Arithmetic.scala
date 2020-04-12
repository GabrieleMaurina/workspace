import scala.util.parsing.combinator._
import scala.io.Source.fromFile
object Arithmetic{
	class Arithmetic extends JavaTokenParsers{
		val 
		def all = rep(expr)
		def expr = 
	}
	def main(args:Array[String]){
		val src = fromFile(args(0))
		val input = src.mkString
		src.close()
		val p = new Arithmetic()
		p.parseAll(, input) match {
			case p.Success(r,_) => println(r)
			case x => println(x)
		}
	}
}
