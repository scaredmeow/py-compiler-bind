import lex_analyzer as lex
import sys

print("Enter Expression: ")
expression = sys.stdin.read()

print("LEXEME\t\t\t\tTOKEN")

errors = []

# expression = '''
# int a,b
# shoot('as)
# as
# '''

for token in lex.tokenize(expression):
  print(str(token.value)+"\t\t"+str(token.type))

errors = token.errors

for i in errors:
  print(i)

