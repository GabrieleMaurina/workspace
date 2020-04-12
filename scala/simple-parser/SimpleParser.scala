import scala.util.parsing.combinator._

class SimpleParser extends JavaTokenParsers{
	def expr:Parser[Double] = sum | sub | num
	def num = floatingPointNumber ^^ {_.toDouble}
	def sum = num ~ "+" ~ expr ^^ {case x ~ _ ~ y => x + y}
	def sub = num ~ "-" ~ expr ^^ {case x ~ _ ~ y => x - y}
}
