# # import ply.lex as lex

# # List of Tokens
# with open("rwords.txt") as f:
#   reserved = f.read()
#   reserved = list(item for item in reserved.split('\n') if item.strip())
# reserved = dict(zip(reserved,reserved))

# tokens = list(reserved.values()) + ['int_literal','neg_int_literal','deci_literal','neg_deci_literal',
#         'char_literal','str_literal','id']

# # states = (
# #     ('whitespace', 'exclusive'),
# #   )


# # A regular expression rule with some action code
# def t_int_literal(t):
#     r'\d(\d|$|^)'
#     t.value = int(t.value)    
#     return t

# # def t_whitespace(t):
# #     r'[a-z](\w|$|^){14}'                       # Initial brace level
# #     t.lexer.begin('whitespace')  

# # def t_whitespace_id(t):
# #     r'\s'
# #     t.type = reserved.get(t.value,'id')    # Check for reserved words
# #     t.lexer.begin('INITIAL')
# #     return t

# def t_id(t):
#     r'[a-z](\w|$|^){14}' 
#     t.type = reserved.get(t.value,'id')    # Check for reserved words
#     t.lexer.begin('INITIAL')
#     return t

# # Define a rule so we can track line numbers
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# # A string containing ignored characters 
# t_ignore  = ' \t#'

# # Error handling rule
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)

# # Build the lexer
# lexer = lex.lex()

# data = input("Enter String: ")

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok) # type = token, value = original token value, lineno = vertical line no, lexpos = horizontal 

