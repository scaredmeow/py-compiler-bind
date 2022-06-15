import lexical

# First Set
first_comm = ["comment"]
first_global_dec = ["const", "classic", "sheriff",
                    "agent", "roster", "map", "site", "omen"]
first_const_dec = ["const"]
first_const_dec1 = [","]
first_data_type = ["classic", "sheriff", "agent", "roster", "map"]
first_value = ["classic_literal", "neg_classic_literal", "sheriff_literal",
               "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first_map_lit = ["attack", "defend"]
first_conc = ["&"]
first_var_dec = ["classic", "sheriff", "agent", "roster", "map"]
first_init = ["="]
first_var_dec1 = [","]
first_array_dec = ["classic", "sheriff", "agent", "roster", "map"]
first_index = ["classic_literal", "id"]
first_func_stmt = ["id"]
first_args = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal",
              "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first_variable = ["id"]
first_more_args = [","]
first_array_elem = ["id"]
first_array_index2 = ["["]
first_array_index3 = ["["]
first_struct_elem = ["id"]
first_array_value = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                     "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend", "{"]
first_array_value1 = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                      "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first_more_array = [","]
first_array_value2 = ["{"]
first_more_array2 = [","]
first_array_value3 = ["{"]
first_more_array3 = [","]
first_struct_dec = ["site"]
first_site_element = ["classic", "sheriff", "agent", "roster", "map"]
first_more_element = ["classic", "sheriff", "agent", "roster", "map"]
first_site_var = ["id"]


# Follow Set


var = "hi"


def parser(expression):
    lex = lexical.lexer(expression)
    token_type = lex.type
    token_value = lex.value
    token_error = lex.error
    token_column = lex.column
    token_line = lex.line
    syntax_error = []
    lex_error_count = count = 0
    for i in token_error:
        if i != '':
            count += 1

    if 'lex-error' in token_type:
        for index, item in enumerate(token_type):
            if item == 'lex-error' and token_value[index] == 'lex-error':
                lex_error_count += 1
        syntax_error.append(
            f'Syntax Error on Ln 0, Col 0: Syntax Analyzer can\'t continue there {"is "+str(count-lex_error_count)+" Lexical Error, " if count-lex_error_count == 1 else "are "+str(count-lex_error_count)+" Lexical Errors,"} \nplease check lexical analyzer first!')
        return syntax_error

    for index, item in enumerate(token_type):
        if item == 'lex-error' and token_value[index] == 'lex-error':
            continue
        print(
            f'Line {token_line[index]}, Column {token_column[index]}: {item}: {token_value[index]}: {token_error[index]}')
    return token_type


# token_type = parser(lexemes)
# print(token_type)

# TODO: Add Parser
