import scala.util.parsing.combinator._

class CalculatorParser extends JavaTokenParsers{
	def file = rep(expr) ^^ {case _ => }
	def expr = num | sum | sub
	def num = floatingPointNumber ^^ {_.toDouble}
	def sum = expr ~ "+" ~ expr ^^ {case x ~ y => x + y}
	def sub = expr ~ "-" ~ expr ^^	{case x ~ y => x - y}
}
