object Comprehensions{

	def squaredNumbers(obj:Any) : Any = obj match{
		case l:List[_] => for(i <- l; v = squaredNumbers(i); if(v!=null)) yield v
		case i:Int => i*i
		case d:Double => d*d
		case _:Any => null
	}

	def printSquaredNumbers(a:Any) = Console.println("Squared numbers of " + a + " are " + squaredNumbers(a))

	def intersect(l1:List[Any], l2:List[Any]):List[Any] = for(v <- l1 if l2.contains(v)) yield v 

	def printIntersect(l1:List[Any], l2:List[Any]) = Console.println("The intersection of " + l1 + " and " + l2 + " is " + intersect(l1, l2))

	def symmetricDifference(l1:List[Any], l2:List[Any]):List[Any] = for(v <- l1++l2 if(!l1.contains(v) || !l2.contains(v))) yield v

	def printSymmetricDifference(l1:List[Any], l2:List[Any]) = Console.println("The symmetric difference of " + l1 + " and " + l2 + " is " + symmetricDifference(l1, l2))

	def main(args:Array[String]){
		printSquaredNumbers(List(1, 2, 3))
		printSquaredNumbers(List(1, 2, 3, List(2, 3, 4)))
		printSquaredNumbers(List(1, 2.4, 3.5, "asdf"))
		printSquaredNumbers(List(1, 2, 3))
		printSquaredNumbers(List(1, List(1, 3, 4, "qer"), 3))
		printSquaredNumbers(List(1, List(2, 5, List(1, 4.5)), 3, "qwer", 'r'))

		printIntersect(List(1, 2, 3), List(2, 3, 4))
		printIntersect(List(1, 2, 3, 4, 5), List(2, 3, 4))
		printIntersect(List(1, 2, 3), List(4, 5, 6))
		
		printSymmetricDifference(List(1, 2, 3), List(2, 3, 4))
		printSymmetricDifference(List(1, 2, 3, 4, 5), List(2, 3, 4))
		printSymmetricDifference(List(1, 2, 3), List(4, 5, 6))
	}
}
