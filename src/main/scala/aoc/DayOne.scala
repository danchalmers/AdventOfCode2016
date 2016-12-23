package aoc {

  import aoc.Direction._

  /**
    * Created by danc on 23/12/2016.
    */
  object DayOne {
    def convertToDirections(input: String): Seq[(Direction, Int)] = {
      var heading = NORTH

      def turnConvert(turnStep: String): (Direction, Int) = {
        val steps = turnStep.substring(1).toInt
        if (turnStep.charAt(0) == 'R') { heading = turnRight(heading) }
        else { heading = turnLeft(heading) }
        (heading, steps)
      }

      for (turnStep <- input.split(",")) yield turnConvert(turnStep.trim)
    }


  }

}