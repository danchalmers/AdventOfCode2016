import aoc.Direction._
import aoc.DayOne
import org.scalatest.{FlatSpec, Matchers}

/**
  * Created by danc on 23/12/2016.
  */
class DayOneSpec extends FlatSpec with Matchers {
  val test1 = "R2, L3"

  "Interpreting turns" should "give directions and steps" in {
    DayOne.convertToDirections(test1) should be (List[(Direction, Int)]((EAST, 2), (NORTH, 3)))

  }
}
