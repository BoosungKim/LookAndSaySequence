import scala.io.StdIn

/**
  * Created by busungkim on 2017. 2. 20..
  */
object LookAndSaySequence {

  def main(args: Array[String]): Unit = {
    val n = StdIn.readInt

    def solve(n: Int, seq: Seq[Char]): Seq[Char] = {

      def produce(c: Char, n: Int)(seq: Seq[Char]): Seq[Char] = seq match {
        case Nil => Seq((n+'0').toChar, c)
        case h :: tail =>
          if(c == h) produce(c, n+1)(tail) else Seq((n+'0').toChar, c) ++ produce(h, 1)(tail)
      }

      if(n <= 1) seq else solve(n-1, produce(seq.head, 0)(seq))
    }

    print(solve(n, Seq('1')).mkString)
  }
}
