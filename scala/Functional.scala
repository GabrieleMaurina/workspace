object Functional{

	def isPalindrome(s:String) : Boolean = {
		palindrome(s, 0, s.length()/2, s.length()-1)
	}

	private def palindrome(s:String, i:Int, h:Int, l:Int) : Boolean = {
		if(i < h)
			if(s(i)==s(l-i)) palindrome(s, i+1, h, l)
			else false
		else true
	}

	def printPalindrome(s:String){
		if(isPalindrome(s)) Console.println("\"" + s + "\" IS palindrome")
		else Console.println("\"" + s + "\" is NOT palindrome")
	}

	def factors(n:Int) : List[Int] = {
	 	facts(n, 1, List[Int]()).reverse
	}

	private def facts(n:Int, i:Int, l:List[Int]) : List[Int] = {
		if(i <= n){
			if(n%i == 0) facts(n, i+1, i::l)
			else facts(n, i+1, l)
		}
		else l
	}

	def printFactors(n:Int){
		Console.println("Factors of " + n + " are: " + factors(n))
	}

	def isProper(n:Int) = (n+n) == factors(n).sum

	def printProper(n:Int) = if(isProper(n)) Console.println(n + " IS proper") else Console.println(n + " is NOT proper")

	def isAnagram(s:String, d:List[String]) = d.exists((e) => anagram(s, e))

	private def anagram(s1:String, s2:String) : Boolean = (s1,s2) match{
		case ("", "") => true
		case _ if s1.length != s2.length => false
		case _ => anagram(s1.substring(1), s2.replaceFirst(s1.substring(0,1), ""))
	}

	def printAnagram(s:String, d:List[String]){
		if(isAnagram(s,d)) Console.println("AN anagram of \"" + s + "\" is in " + d)
		else Console.println("NO anagram of \"" + s + "\" is in " + d)
	}

	def main(args:Array[String]){
		printPalindrome("asdf")
		printPalindrome("asdfdsa")
		printPalindrome("asdfdsas")
		printPalindrome("ciaociao")
		printPalindrome("asdffdsa")
		printPalindrome("wowow")
		printPalindrome("")

		printFactors(1)
		printFactors(2)
		printFactors(6)
		printFactors(12)
		printFactors(24)
		printFactors(17)
		printFactors(19)
		printFactors(36)

		printProper(1)
		printProper(2)
		printProper(3)
		printProper(6)
		printProper(10)

		printAnagram("asdf", List("asdf", "qwer"))
		printAnagram("asdf", List("fdas", "qwer"))
		printAnagram("asdf", List("", "qwer", "qweadsf"))
		printAnagram("asdf", List("zxcv", "qwer"))
		printAnagram("asdf", List("asd", "qwer"))
		printAnagram("asdf", List("asdff", "qwer"))
		printAnagram("asdf", List("asd", "asfd"))
		printAnagram("asdf", List("asd", "qwerasdf"))
		printAnagram("asdf", List("asdasdf", "qwer"))
		printAnagram("asdf", List("asdqwer", "asdfqwer", "freas", "fdsa"))
	}
}
