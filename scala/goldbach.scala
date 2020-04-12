import scala.util.control.Breaks._

object goldbatch{

	private def primes(n:Int):List[Int] = {
		var ps = List(2)
		for(x <- 2 until n){
			var div = false
			breakable{
				for(p <- ps){
					if(x%p == 0){
						div = true
						break
					}
				}
			}
			if(!div) ps = x::ps
		}
		ps
	}

	def goldbatch(n:Int):(Int, Int) = {
		val p = primes(n)
		(for(x <- p; y <- p; if(x+y == n)) yield (x,y)).head
	}

	def printGoldbatch(n:Int) = Console.println("The Goldbatch partition of " + n + " is " + goldbatch(n))

	def main(args:Array[String]){
		printGoldbatch(4)
		printGoldbatch(6)
		printGoldbatch(8)
		printGoldbatch(10)
		printGoldbatch(12)
		printGoldbatch(14)
		printGoldbatch(16)
		printGoldbatch(18)
		printGoldbatch(20)
		printGoldbatch(30)
		printGoldbatch(100)
	}
}
