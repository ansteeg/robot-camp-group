import java.nio.file.{Files, Paths}
import scala.util.Try

object Main {
  def main(args: Array[String]): Unit = {
    val filePath = "data6.txt"
    val lines = scala.io.Source.fromFile(filePath).getLines().toList
    val outputLines = lines.zipWithIndex.map {
      case (line, 0) => s"${line.replace("\r", "")},Comments"
      case (line, _) =>
        val cleaned = line.replace("\r", "")
        val parts = cleaned.split(",")
        if (parts.length < 8) line // skip invalid lines
        else {
          val summary = parts(6)
          val evaluation = parts(7).toFloat
          val comments = (summary, evaluation) match {
            case ("super", e) if e >= 3 => "Excellent"  
            case ("super", _) => "Good but inconsistent"
            case (_, e) if e >= 2 => "Promising"  
            case _ => "Needs Improvement"
          }
          s"$cleaned,$comments"
        }
    }

    Files.write(Paths.get("data7.txt"), outputLines.mkString("\n").getBytes)
  }
}
