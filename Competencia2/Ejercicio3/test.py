from antlr4 import *
from ExprLexer import ExprLexer
import sys

# Obtiene la entrada y la separa en tokens
input_stream = FileStream(sys.argv[1])

lexer = ExprLexer(input_stream)

# Guarda los tokens generados por el lexer
tokens = CommonTokenStream(lexer)
tokens.fill()

print(f"{'LEXEMA':<15} {'TOKEN':<15} {'TIPO':<6} {'LINEA':<8} {'COLUMNA':<8}")
print("-" * 60)

for token in tokens.tokens:

    # Ignorar EOF
    if token.type == Token.EOF:
        continue

    nombre_token = lexer.symbolicNames[token.type]

    print(f"{token.text:<15} {nombre_token:<15} {token.type:<6} {token.line:<8} {token.column:<8}")