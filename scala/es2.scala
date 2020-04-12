import scala.util.parsing.combinator._

abstract class Operation{
	def calc(v: Double): Double
	def setVal2(val2: Double): Operation = {this}
}

class Identity extends Operation{
	override def calc(v: Double): Double = v
}

class Plus extends Operation{
	var val2: Double = 0
	
	override def setVal2(val2: Double): Operation = {
		this.val2 = val2
		this
	}
	
	override def calc(v: Double): Double = v + this.val2	
}

class Minus extends Operation{
	var val2: Double = 0
	
	override def setVal2(val2: Double): Operation = {
		this.val2 = val2
		this
	}
	
	override def calc(v: Double): Double = v - this.val2	
}

class Mul extends Operation{
	var val2: Double = 0
	
	override def setVal2(val2: Double): Operation = {
		this.val2 = val2
		this
	}
	
	override def calc(v: Double): Double = v * this.val2	
}

class Div extends Operation{
	var val2: Double = 0
	
	override def setVal2(val2: Double): Operation = {
		this.val2 = val2
		this
	}
	
	override def calc(v: Double): Double = v / this.val2	
}

class ExpressionParser extends JavaTokenParsers {
	def expression: Parser[Double] = term ~ seq ^^ {case t~s => s.calc(t)}
	def term: Parser[Double] = fin ~ opprior ~ fin ^^ {case a1~op~a2 => op.setVal2(a2).calc(a1)} | fin
	def fin: Parser[Double] = floatingPointNumber ^^ {_.toDouble}
	def seq: Parser[Operation] =  continue | "" ^^ {_ => new Identity}
	def continue: Parser[Operation] = op ~ expression ^^ {case o~e => o.setVal2(e)}
	def op: Parser[Operation] = "+" ^^ {_ => new Plus} | "-" ^^ {_ => new Minus}
	def opprior: Parser[Operation] = "*" ^^ {_ => new Mul} | "/" ^^ {_ => new Div}
}


object es2{
	def main(args: Array[String]):Unit = {
		val exp1 = "1 * 3 + 1 * 2"
		
		val parser = new ExpressionParser
		parser.parseAll(parser.expression, exp1) match {
			case parser.Success(r, _) => println("Success -> " + r.toString)	
			case x => println(x)
		}
	}
}
