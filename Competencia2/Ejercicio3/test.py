from antlr4 import*
from ExprLexer import ExprLexer
from ExprParser import ExprParser


entrada = "X = 10"

input_stream = InputStream(entrada)

lexer = ExprLexer(input_stream)

stream = CommonTokenStream(lexer)

parser = ExprParser(stream)

parser.root()

print("Análisis terminado")