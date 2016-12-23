package aoc {

  /**
    * Created by danc on 23/12/2016.
    */

  object Direction extends Enumeration {
    type Direction = Value
    type Move = (Direction, Int)
    /**
      * Position is Eastings, Northings like a map
      */
    type Position = ((Int, Int))

    val ORIGIN: Position = (0, 0)

    val NORTH, EAST, SOUTH, WEST = Value

    def turnRight(dir: Direction): Direction = {
      Direction((dir.id + 1) % 4)
    }

    def turnLeft(dir: Direction): Direction = {
      Direction((4 + dir.id - 1) % 4)
    }

    def move(move: Move, position: Position = ORIGIN): Position = {
      val (dir, steps) = move
      var (posE, posN) = position
      dir match {
        case EAST => posE = posE + steps
        case WEST => posE = posE - steps
        case NORTH => posN = posN + steps
        case SOUTH => posN = posN - steps
      }
      (posE, posN)
    }

  }

}