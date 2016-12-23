import aoc.Direction
import aoc.Direction._
import org.scalatest.{FlatSpec, Matchers}

/**
  * Created by danc on 23/12/2016.
  */
class DirectionSpec extends FlatSpec with Matchers {
  "Given a direction, a turn right" should "turn north into east" in {
    Direction.turnRight(NORTH) should be (EAST)
  }

  it should "turn west into north" in {
    Direction.turnRight(WEST) should be (NORTH)
  }

  "Given a direction, a turn left" should "turn north into west" in {
    Direction.turnLeft(NORTH) should be (WEST)
  }

  it should "turn west into south" in {
    Direction.turnLeft(WEST) should be (SOUTH)
  }

  "From the origin a move" should "change the position" in {
    Direction.move((NORTH, 2): Move) should be ((0, 2))
    Direction.move((SOUTH, 2): Move) should be ((0, -2))
    Direction.move((EAST, 1): Move) should be ((1, 0))
    Direction.move((WEST, 3): Move) should be ((-3, 0))
  }

  "From a position a move across axes" should "change the position and axis label" in {
    val pos1: Position = (1, 1)
    val pos2: Position = (-1, -1)
    Direction.move((SOUTH, 2): Move, pos1) should be ((1, -1))
    Direction.move((NORTH, 2): Move, pos2) should be ((-1, 1))
    Direction.move((WEST, 2): Move, pos1) should be ((-1, 1))
    Direction.move((EAST, 2): Move, pos2) should be ((1, -1))
  }
}
