import aoc.Direction.{Direction, _}
import aoc.{DayOne, Direction}
import org.scalatest.{FlatSpec, Matchers}

/**
  * Created by danc on 23/12/2016.
  */
class DayOneSpec extends FlatSpec with Matchers {
  val test1 = "R2, L3"
  val test2 = "R2, R2, R2"
  val test3 = "R5, L5, R5, R3"
  val testInput = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"

  "Interpreting turns" should "give directions and steps" in {
    DayOne.convertToDirections(test1) should be ( List[(Direction, Int)] ((EAST, 2), (NORTH, 3)) )
    DayOne.convertToDirections(test2) should be ( List[(Direction, Int)] ((EAST, 2), (SOUTH, 2), (WEST, 2)) )
  }

  "Calculating position" should "give steps north and east" in {
    DayOne.calcPosition(test1) should be ((2, 3))
  }

  "Calculating distance" should "give steps for Manhattan distance" in {
    DayOne.calcDistance(test1) should be (5)
    DayOne.calcDistance(test2) should be (2)
    DayOne.calcDistance(test3) should be (12)
  }

  "The answer to Advent of Code day one" should "be the distance for testInput" in {
    val position = DayOne.calcPosition(testInput)
    val distance = DayOne.calcDistance(position)
    println(f"Position $position is $distance steps away")
    succeed
  }
}
