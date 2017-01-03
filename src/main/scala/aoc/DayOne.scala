package aoc {

  import aoc.Direction._

  /**
    * Created by danc on 23/12/2016.
    * Learning Scala via the advent of code
    * Problem spec at http://adventofcode.com/2016/day/1
    */

  object DayOne {
    /**
      * Convert input to a sequence of moves N/S/E/W + steps
      * @param input  a sequence of comma separated L/R turn + steps pairs in a string
      * @return a sequence of Moves
      */
    def convertToDirections(input: String): Seq[Move] = {
      var heading = NORTH

      def turnConvert(turnStep: String): Move = {
        val steps = turnStep.substring(1).toInt
        if (turnStep.charAt(0) == 'R') { heading = turnRight(heading) }
        else { heading = turnLeft(heading) }
        (heading, steps)
      }

      for (turnStep <- input.split(",")) yield turnConvert(turnStep.trim)
    }

    /**
      * Calculate the final position from a sequence of moves, assuming starting at origin
      * East and North are positive
      * @param headingSteps  a sequence of Moves
      * @return an East, North position
      */
    def calcPosition(headingSteps: Seq[Move]): Position = {
      var pos: Position = ORIGIN
      for (move <- headingSteps) {
        pos = Direction.move(move, pos)
      }
      pos
    }

    /**
      * Calculate the final position from input string
      * @param input  a sequence of comma separated L/R turn + steps pairs in a string
      * @return East, North
      */
    def calcPosition(input: String): Position = {
      calcPosition(convertToDirections(input))
    }

    /**
      * Calculate the Manhattan distance from origin from input string
      * @param input  a sequence of comma separated L/R turn + steps pairs in a string
      * @return distance in blocks
      */
    def calcDistance(input: String): Int = {
      calcDistance(calcPosition(input))
    }

    /**
      * Calculate the Manhattan distance from origin from a position
      * @param position  A position on a city grid
      * @return distance in blocks
      */
    def calcDistance(position: Position): Int = {
      val (east, north) = position
      east.abs + north.abs
    }

    def smallSteps(headingSteps: Seq[Move]): Seq[Position] = {
      var startPos = ORIGIN
      var smallSteps:Seq[Position] = Seq()
      for (step <- headingSteps) {
        for (smallStep <- moves(step, startPos)) {
          smallSteps = smallSteps :+ smallStep
          startPos = smallStep
        }
      }
      smallSteps
    }

    def calcFirstPlaceVistedTwice(headingSteps: Seq[Move]): Position = {
      var visited: Set[Position] = Set(ORIGIN)
      val posSteps = smallSteps(headingSteps)

      def makeMove(poss: Seq[Position]): Position = {
        var pos = poss.head
        if (!(visited contains pos)) {
          visited = visited + pos
          pos = makeMove(poss.tail)
        }
        pos
      }

      makeMove(posSteps)
    }

  }

}