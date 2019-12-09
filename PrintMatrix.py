import MatrixDriver as Matrix
import MatrixCharacters as Chars
import sys

Matrix.initialiseDisplays(5)
if (len(sys.argv) > 1):
    Matrix.sendMessage(Chars.Parse(sys.argv[1]))

