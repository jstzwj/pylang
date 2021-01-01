import sys
from antlr4 import *
from grammar.Python3Lexer import Python3Lexer
from grammar.Python3Parser import Python3Parser
 
def main(argv):
    input_stream = FileStream("setup.py")
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    print(tree)
 
if __name__ == '__main__':
    main(sys.argv)