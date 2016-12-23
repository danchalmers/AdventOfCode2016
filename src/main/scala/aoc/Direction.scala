package aoc {

  /**
    * Created by danc on 23/12/2016.
    */
  object Direction extends Enumeration {
    type Direction = Value
    val NORTH, EAST, SOUTH, WEST = Value

    def turnRight(dir: Direction): Direction = {
      Direction((dir.id + 1) % 4)
    }

    def turnLeft(dir: Direction): Direction = {
      Direction((4 + dir.id - 1) % 4)
    }
  }

}