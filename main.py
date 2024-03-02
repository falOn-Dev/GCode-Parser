from GCodeVisitor import GCodeVisitor
from generated_code.gcode_grammarLexer import gcode_grammarLexer
from generated_code.gcode_grammarParser import gcode_grammarParser
from antlr4 import InputStream, CommonTokenStream

def main():
    input_data = "G0 X0 Y0 Z0 E50 F50\nG1 X300 F300 E300"
    input_stream = InputStream(input_data)
    lexer = gcode_grammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gcode_grammarParser(token_stream)
    tree = parser.program()

    visitor = GCodeVisitor()
    visitor.visitProgram(tree)



if __name__ == '__main__':
    main()