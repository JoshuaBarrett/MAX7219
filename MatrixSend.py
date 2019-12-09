import MatrixDriver as Matrix
import MatrixCharacters as Chars
import sys

print('test')
print(sys.argv)
if len(sys.argv) > 1:
    Matrix.initialiseChannels()
    Matrix.sendMessage(Chars.Parse(sys.argv[1]))
