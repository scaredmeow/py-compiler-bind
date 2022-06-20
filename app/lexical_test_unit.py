import lexical as lex
list_of_text = ["agent~", "roster\"", "map~", "site~", "omen~"]

for i in list_of_text:
    error = lex.lexer(i).error
    print(error)
