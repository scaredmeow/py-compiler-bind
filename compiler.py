import bind.lex as lex
import sys

print("Enter Expression: ")
expression = sys.stdin.read()

# expression = '''
# int a,b
# shoot('as)
# as
# '''

print("LEXEME\t\t\t\tTOKEN")
for token in lex.tokenize(expression):
  print(str(token.value)+"\t\t\t\t"+str(token.type))

errors = []
errors = token.errors

for i in errors:
  print(i)

