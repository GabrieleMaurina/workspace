import scala.util.parsing.combinator._

class BetterParser extends JavaTokenParsers{
	def expr:Parser[Double] = expr ~ "+" ~ term ^^ {case x ~ _ ~ y => x+y} | expr ~ "-" ~ term ^^ {case x ~ _ ~ y => x-y} | term
	def term:Parser[Double] = term ~ "*" ~ fact ^^ {case x ~ _ ~ y => x*y} | term ~ "/" ~ fact ^^ {case x ~ _ ~ y => x/y} | fact
	def fact:Parser[Double] = floatingPointNumber ^^ {_.toDouble} | "(" ~> expr <~ ")" | "-" ~> fact ^^ {case x => -x}
}
