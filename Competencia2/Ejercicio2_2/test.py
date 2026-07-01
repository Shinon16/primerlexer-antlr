# Importa ANTLR4 para funciones
from antlr4 import *
from ExprLexer import ExprLexer
import sys
# Lo quw obtienes es la entrada, analiza el texto y lo separa en tokens
input_stream = FileStream(sys.argv[1])
lexer = ExprLexer(input_stream)

# Toma los tokens que produjo el lexer 
tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto ", token.text)
    print("Tipo ", token.type)
    print("Linea ", token.line)
    print("Columna ", token.column)
    nombre = lexer.symbolicNames[token.type]
    print("Nombre ", nombre)