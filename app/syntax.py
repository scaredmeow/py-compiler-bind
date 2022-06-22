import lexical
from production import FirstSet, GrammarRules, FollowSet
import helper as hp


def parser(expression):
    lex = lexical.lexer(expression)
    token_type = lex.type
    token_value = lex.value
    token_error = lex.error
    token_column = lex.column
    token_line = lex.line
    syntax_error = []
    lex_error_count = count = 0
    f = FirstSet()
    g = GrammarRules()
    fs = FollowSet()
    if 'lex-error' in token_type:
        for i in token_error:
            if i != '':
                count += 1
        for index, item in enumerate(token_type):
            if item == 'lex-error' and token_value[index] == 'lex-error':
                lex_error_count += 1
        syntax_error.append(
            f'Syntax Error on Ln 0, Col 0: Syntax Analyzer can\'t continue there {"is "+str(count-lex_error_count)+" Lexical Error, " if count-lex_error_count == 1 else "are "+str(count-lex_error_count)+" Lexical Errors,"} \nplease check lexical analyzer first!')
        return syntax_error

    token_length = len(token_type)
    current_token = ctr = 0
    production = "program"

    # while current_token < token_length:
    #     pass

    print(f"{len(token_type)}: {len(token_error)}: {len(token_value)}")
    # for index, item in enumerate(token_type):
    #     print(
    #         f'Line {token_line[index]}, Column {token_column[index]}: {item}: {token_value[index]}: {token_error[index]}')
    return token_type


parser("""hello classic""")

# first_set (token, production)
# If true and non-terminal, add to stack
# if true and terminal, continue to the next rule in production and add one to the current token pointer
# if false then proceed to the next item in current production


# list_of_token
# ctr = 0
# production = "program"
# temp_stack = []

# comment: 0
# global_dec : 1
# temp_stack [global_dec, 1]
# ctr = 0
# production: global_dec

# global_dec = []
# const_dec ; global_dec


# if ["nul"] in g.cfg["global_dec"]:
#     print("hi")
# print(f.first)
# print(g.cfg)
# print(fs.follow)

# RES_WORDS = hp.readFile("tokens/res-words.txt")
# RES_SYMBOLS = hp.readFile("tokens/res-symbols.txt")
# RES_TOKENS = ["comment", "classic_literal", "neg_classic_literal", "sheriff_literal",
#               "neg_sheriff_literal", "agent_literal", "roster_literal"]
# non_terminal = g.non_terminal
# terminal = RES_SYMBOLS + RES_WORDS + RES_TOKENS
# print(terminal)
