from re import template
import lexical
from production import FirstSet, GrammarRules, FollowSet
import helper as hp

f = FirstSet()
g = GrammarRules()
fs = FollowSet()

RES_WORDS = hp.readFile("tokens/res-words.txt")
RES_SYMBOLS = hp.readFile("tokens/res-symbols.txt")
RES_TOKENS = ["comment", "classic_literal", "neg_classic_literal", "sheriff_literal",
              "neg_sheriff_literal", "agent_literal", "roster_literal", "id"]
terminal = RES_SYMBOLS + RES_WORDS + RES_TOKENS
non_terminal = g.non_terminal


def parser(expression):
    lex = lexical.lexer(expression)
    token_type = lex.type
    token_value = lex.value
    token_error = lex.error
    token_column = lex.column
    token_line = lex.line
    syntax_error = []
    lex_error_count = count = 0

    token_type = [i for i in token_type if i != "whitespace"]
    for index, item in enumerate(token_type):
        if item.lower().find("id") != -1:
            token_type[index] = "id"

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

    current_token = rule_ptr = production_ptr = 0
    production = "program"
    current_production = g.cfg[production][production_ptr]
    stack_production = []
    is_error = False
    token_length = len(token_type)
    print(token_length)
    while current_token <= token_length:
        # print(f'current_token: {token_type[current_token]}')
        print(token_type)
        print(f'current_token: {current_token}, current_production: {current_production}, production: {production}, rule_ptr: {rule_ptr}, production_ptr: {production_ptr}')
        print(f"stack_production: {stack_production}")
        if current_token < token_length:
            if len(current_production) == rule_ptr and stack_production:
                rule_ptr = stack_production.pop() + 1
                current_production = stack_production.pop()
                production = stack_production.pop()

            else:
                if current_production[rule_ptr] == "comm":
                    if token_type[current_token] == "comment":
                        current_token += 1
                    else:
                        if fs.follow_set(token_type[current_token], current_production[rule_ptr]):
                            rule_ptr += 1
                        else:
                            syntax_error.append(
                                f'Syntax Error on Ln {token_line[current_token]}, Col {token_column[current_token]}:  Expected {str(current_production[rule_ptr]) if len(current_production) - 1 == rule_ptr else current_production[rule_ptr+1]} here, "{token_type[current_token].upper()+"- "+token_value[current_token] if token_type[current_token].find("id") != -1 else token_value[current_token]}" is detected!')
                            is_error = True
                elif current_production[rule_ptr] in non_terminal:
                    if f.first_set(token_type[current_token], current_production[rule_ptr]):
                        stack_production.append(production)
                        stack_production.append(current_production)
                        stack_production.append(rule_ptr)
                        production = current_production[rule_ptr]
                        # is_reprocicable = False
                        # production_length = len(g.cfg[production])
                        # if production_length != len(set([frozenset(i) for i in g.cfg[production]])):
                        #     is_reprocicable = True
                        for i in g.cfg[production]:
                            temp_list = []
                            if "var_dec" in i or "array_dec" in i:
                                print("asdasdadasdasasdas")
                                print(
                                    f'token: {token_type[current_token+1]}production{g.cfg[i[0]][0]}')
                                if token_type[current_token+1] in g.cfg[i[0]][0]:
                                    current_production = i
                                    break
                                else:
                                    continue
                            else:
                                temp_list = [
                                    x for x in i if x not in stack_production]
                            print(f'1: {temp_list}')

                            if token_type[current_token] in temp_list:
                                print("hello")
                                current_production = i
                                break
                            else:
                                print("hi")
                                temp_list = [
                                    x for x in temp_list if x not in terminal]
                                if f.first_set(token_type[current_token], i[0]):
                                    current_production = i
                                    break
                                # for item in temp_list:

                                #     if f.first_set(token_type[current_token], item):
                                #         current_production = i
                                #         is_found = True
                                #         print(
                                #             f"token type: {token_type[current_token]}")
                                #         print(f'2: {temp_list}')
                                #         break
                                #     if is_reprocicable:
                                #         break
                                # if is_found:
                                #     break
                        rule_ptr = 0
                    else:
                        if "null" in f.first[current_production[rule_ptr]] and fs.follow_set(token_type[current_token], current_production[rule_ptr-1]):
                            print("hi")
                            rule_ptr += 1
                        else:
                            if fs.follow_set(token_type[current_token], current_production[rule_ptr]):
                                rule_ptr += 1
                            else:
                                syntax_error.append(
                                    f'Syntax Error on Ln {token_line[current_token]}, Col {token_column[current_token]}:  Expected {str(current_production[rule_ptr]) if len(current_production) - 1 == rule_ptr else current_production[rule_ptr+1]} here, "{token_type[current_token].upper()+"- "+token_value[current_token] if token_type[current_token].find("id") != -1 else token_value[current_token]}" is detected!')
                                is_error = True
                elif current_production[rule_ptr] in terminal:
                    if token_type[current_token] == current_production[rule_ptr]:
                        current_token += 1
                        rule_ptr += 1
                    else:
                        syntax_error.append(
                            f'Syntax Error on Ln {token_line[current_token]}, Col {token_column[current_token]}:  Expected {str(current_production[rule_ptr]) if len(current_production) - 1 == rule_ptr else current_production[rule_ptr+1]} here, "{str(token_type[current_token].upper())+" - "+str(token_value[current_token+1]) if token_type[current_token].find("id") != -1 else token_value[current_token]}" is detected!')
                        is_error = True
        else:
            break
        if is_error:
            return syntax_error

        # print(current_production[rule_ptr])
        # print(f.first_set(token_type[current_token],
        #       current_production[rule_ptr]))
        # rule_ptr += 1

    # print(f"{len(token_type)}: {len(token_error)}: {len(token_value)}")
    # for index, item in enumerate(token_type):
    #     print(
    #         f'Line {token_line[index]}, Column {token_column[index]}: {item}: {token_value[index]}: {token_error[index]}')
    # print(stack_production)
    return []


# print(parser("""hello classic"""))

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


# print(terminal)
