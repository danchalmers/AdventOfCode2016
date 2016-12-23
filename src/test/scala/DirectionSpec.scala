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

}
