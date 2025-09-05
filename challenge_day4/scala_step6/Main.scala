import java.nio.file.{Files, Paths}
import scala.util.{Try, Using}

object Main {
  def main(args: Array[String]): Unit = {
    // Prefer passing files as args; fallback to defaults
    val inPath  = args.lift(0).getOrElse("../testdata/data6.txt")
    val outPath = args.lift(1).getOrElse("../testdata/data7.txt")

    val lines = Using.resource(scala.io.Source.fromFile(inPath))(_.getLines().toList)

    val outputLines = lines.zipWithIndex.map {
      case (line, 0) =>
        s"$line,Comments" // header + new column

      case (line, _) =>
        val parts = line.split(",", -1) // keep empty fields
        // We need at least 9 columns to read parts(7) and parts(8)
        if (parts.length < 9) line
        else {
          val summary     = parts(7).trim
          val evaluationF = Try(parts(8).toFloat).getOrElse(Float.NaN)

          val comments =
            if (summary == "super" && evaluationF >= 3.0f) "Excellent"
            else if (summary == "super")                  "Good but inconsistent"
            else if (!evaluationF.isNaN && evaluationF >= 2.0f) "Promising"
            else "Needs Improvement"

          s"$line,$comments"
        }
    }

    Files.write(Paths.get(outPath), outputLines.mkString("\n").getBytes("UTF-8"))
  }
}
