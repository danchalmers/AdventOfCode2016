package aoc {

  import aoc.Direction._

  /**
    * Created by danc on 23/12/2016.
    */
  object DayOne {
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

    def calcPosition(input: String): Position = {
      var pos: Position = (0, 0)

      val headingSteps = convertToDirections(input)
      for (move <- headingSteps) {
        pos = Direction.move(move, pos)
      }
      pos
    }

    def calcDistance(input: String): Int = {
      calcDistance(calcPosition(input))
    }

    def calcDistance(position: Position): Int = {
      val (east, north) = position
      east.abs + north.abs
    }

  }

}