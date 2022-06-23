from numpy import product
import lexical
from production import FirstSet, GrammarRules, FollowSet
import helper as hp

f = FirstSet()
g = GrammarRules()
fs = FollowSet()

RES_WORDS = hp.readFile("tokens/res-words.txt")
RES_SYMBOLS = hp.readFile("tokens/res-symbols.txt")
RES_TOKENS = ["comment", "classic_literal", "neg_classic_literal", "sheriff_literal",
              "neg_sheriff_literal", "agent_literal", "roster_literal"]
non_terminal = g.non_terminal


def parser(expression):
    lex = lexical.lexer(expression)
    token_type = lex.type
    token_value = lex.value
    token_error = lex.error
    token_column = lex.column
    token_line = lex.line
    token_length = len(token_type)
    syntax_error = []
    lex_error_count = count = 0

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

    current_token = rule_ptr = 0
    production = "program"
    current_production = g.cfg[production][0]
    stack_production = []

    while current_token < token_length:
        if current_production[rule_ptr] in non_terminal:
            if f.first_set(token_type[current_token], current_production[rule_ptr]):
                stack_production.append(current_production)
                stack_production.append(rule_ptr)
                production = current_production[rule_ptr]
                current_production = g.cfg[production][0]
                rule_ptr = 0
            # else if
            # if ["null"] in g.cfg[current_production]:
            pass

        print(current_production[rule_ptr])
        print(f.first_set(token_type[current_token],
              current_production[rule_ptr]))
        rule_ptr += 1
        current_token += 1

    print(f"{len(token_type)}: {len(token_error)}: {len(token_value)}")
    # for index, item in enumerate(token_type):
    #     print(
    #         f'Line {token_line[index]}, Column {token_column[index]}: {item}: {token_value[index]}: {token_error[index]}')
    print(stack_production)
    return token_type


parser("""hello classic""")

# first_set (token, production)
# If true and non-terminal, add to stack
# if true and terminal, continue to the next rule in production and add one to the current token pointer
# if false then proceed to the next item in current production


# list_of_token
# rule_ptr = 0
# production = "program"
# temp_stack = []

# comment: 0
# global_dec : 1
# temp_stack [global_dec, 1]
# rule_ptr = 0
# production: global_dec

# global_dec = []
# const_dec ; global_dec


# if ["nul"] in g.cfg["global_dec"]:
#     print("hi")
# print(f.first)
# print(g.cfg)
# print(fs.follow)


# terminal = RES_SYMBOLS + RES_WORDS + RES_TOKENS
# print(terminal)
