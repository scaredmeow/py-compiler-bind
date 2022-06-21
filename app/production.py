# Backus Naur Form
# Program ::= comment

# global
# local
# statement

first = {}
follow = {}

# First Set
first["comm"] = ["comment", "null"]
first["global_dec"] = ["const", "classic", "sheriff",
                       "agent", "roster", "map", "site", "omen"]
first["const_dec"] = ["const"]
first["const_dec1"] = [","]
first["data_type"] = ["classic", "sheriff", "agent", "roster", "map"]
first["value"] = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                  "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first["map_lit"] = ["attack", "defend"]
first["conc"] = ["&"]
first["var_dec"] = ["classic", "sheriff", "agent", "roster", "map"]
first["init"] = ["="]
first["var_dec1"] = [","]
first["array_dec"] = ["classic", "sheriff", "agent", "roster", "map"]
first["index"] = ["classic_literal", "id"]
first["func_stmt"] = ["id"]
first["args"] = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal",
                 "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first["variable"] = ["id"]
first["more_args"] = [","]
first["array_elem"] = ["id"]
first["array_index2"] = ["["]
first["array_index3"] = ["["]
first["struct_elem"] = ["id"]
first["array_value"] = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                        "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend", "{"]
first["array_value1"] = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                         "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
first["more_array"] = [","]
first["array_value2"] = ["{"]
first["more_array2"] = [","]
first["array_value3"] = ["{"]
first["more_array3"] = [","]
first["struct_dec"] = ["site"]
first["site_element"] = ["classic", "sheriff", "agent", "roster", "map"]
first["more_element"] = ["classic", "sheriff", "agent", "roster", "map"]
first["site_var"] = ["id"]
first["more_var_site"] = [",", "null"]
first["func_dec"] = ["classic", "sheriff", "agent", "roster", "map", "omen"]
first["func_type"] = ["classic", "sheriff", "agent", "roster", "map", "omen"]
first["param"] = ["classic", "sheriff", "agent", "roster", "map", "null"]
first["param1"] = [",", "null"]
first["local_dec"] = ["classic", "sheriff", "agent",
                      "roster", "map", "const", "site", "null"]
first["struct_init"] = ["site"]
first["more_struct"] = [",", "null"]
first["statements"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id", "++", "--", "defuse",
                       "shoot", "if", "switch", "for", "while", "do", "null"]
first["statement1"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id", "++", "--", "defuse",
                       "shoot", "if", "switch", "for", "while", "do"]
first["expre_stmt"] = ["id", "++," "--"]
first["assign_expr"] = ["id"]
first["assign_op"] = ["=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
first["assign_operand"] = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal", "agent_literal",
                           "roster_literal", "attack", "defend", "++," "--", "(", "and", "or", "n"]
first["expre_stmt1"] = ["id", "classic_literal", "neg_classic_literal",
                        "sheriff_literal", "neg_sheriff_literal", "++", "--", "(", "and", "or", "n"]
first["arith_expr"] = ["id", "classic_literal", "neg_classic_literal",
                       "sheriff_literal", "neg_sheriff_literal", "++", "--", "("]
first["arith_operand"] = ["id", "classic_literal", "neg_classic_literal",
                          "sheriff_literal", "neg_sheriff_literal", "++", "--", "("]
first["num_val"] = ["classic_literal", "neg_classic_literal",
                    "sheriff_literal", "neg_sheriff_litera"]
first["una_expr"] = ["++", "--", "id"]
first["una_op"] = ["++", "--"]
first["arith_op"] = ["+", "-", "*", "^", "/", "//", "%"]
first["rela_expr"] = ["id", "classic_literal", "neg_classic_literal",
                      "sheriff_literal", "neg_sheriff_literal", "++", "--", "("]
first["rela_operand"] = ["id", "classic_literal", "neg_classic_literal",
                         "sheriff_literal", "neg_sheriff_literal", "++", "--", "("]
first["rela_op"] = ["==", "=!", "=>", "=<", "<", ">"]
first["log_expr"] = ["and", "or", "n"]
first["log_expr1"] = ["and", "or"]
first["log_expr2"] = ["n"]
first["log_op"] = ["and", "or"]
first["log_operand"] = ["and", "or", "n", "id", "classic_literal", "neg_classic_literal",
                        "sheriff_literal", "neg_sheriff_literal", "++," "--", "(", "attack", "defend"]
first["ret_stmt"] = ["defuse"]
first["ret_operand"] = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal",
                        "agent_literal", "roster_literal", "attack", "defend", "++", "--", "(", "and", "or", "n"]
first["in_stmt"] = ["aim"]
first["in_operand"] = ["id"]
first["out_stmt"] = ["shoot"]
first["out_operand"] = ["id", "\"", "classic_literal", "neg_classic_literal",
                        "sheriff_literal", "neg_sheriff_literal", "++", "--", "(", "and", "or", "n", "fs"]
first["str_form"] = ["{", "null"]
first["str_var"] = ["{", "null"]
first["condi_stmt"] = ["if", "switch"]
first["if_stmt"] = ["if"]
first["condition"] = ["id", "attack", "defend", "classic_literal", "neg_classic_literal",
                      "sheriff_literal", "neg_sheriff_literal", "(", "++", "--", "and", "or", "n"]
first["if_stmt1"] = ["elif", "null"]
first["if_stmt2"] = ["else", "null"]
first["switch_stmt"] = ["switch"]
first["case_literal"] = ["classic_literal", "agent_literal"]
first["more_votes"] = ["vote", "null"]
first["break"] = ["kill", "null"]
first["loop_stmt"] = ["for", "while", "do"]
first["for_stmt"] = ["for"]
first["for_init"] = ["id"]
first["loop_cond"] = ["id", "classic_literal", "neg_classic_literal",
                      "sheriff_literal", "neg_sheriff_literal", "++", "--", "(", "and", "or", "n"]
first["break_con"] = ["revive", "kill"]
first["while_stmt"] = ["while"]
first["dowhile_stmt"] = ["do"]
first["function_def"] = ["plant", "null"]

# Follow Set
follow["comm"] = ["const", "classic", "sheriff", "agent", "roster", "map", "site", "omen", "#", "bound",  "id",  "++", '--',
                  "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "plant", "$", "kill", "revive"]
follow["global_dec"] = ["#", "bound"]
follow["const_dec"] = [";"]
follow["const_dec1"] = [";"]
follow["data_type"] = ["id", "arr"]
follow["value"] = [",", ";", ")", "}"]
follow["map_literal"] = [",", ";", ")", "}"]
follow["conc"] = [",", ";", ")", "}"]
follow["var_dec"] = [";"]
follow["init"] = [",", ";"]
follow["var_dec1"] = [";"]
follow["array_dec"] = [";"]
follow["index"] = ["]"]
follow["func_stmt"] = ["]", ";", "+", "-", "*", "^", "/",
                       "//", "%", ")", "==", "=!", "=>", "=<", ">", "<", ",", ")"]
follow["args"] = [")"]
follow["variable"] = [",", ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!",
                      "=>", "=<", ">", "<", ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow["more_args"] = [")"]
follow["array_elem"] = [",", ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!",
                        "=>", "=<", ">", "<", ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow["array_index2"] = ["[", "id", ",", ")", ".", "+", "-", "*", "^", "/", "//", "%", "==",
                          "=!", "=>", "=<", ">", "<", ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow["array_index3"] = ["id", ",", ")", ".", "+", "-", "*", "^", "/", "//", "%", "==",
                          "=!", "=>", "=<", ">", "<", ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow["struct_elem"] = [",", ")", ".", "+", "-", "*", "^", "/", "//", "%", "==", "=!",
                         "=>", "=<", ">", "<", ";", "++", "--", "=", "=+", "=-", "=*", "=/", "=^", "=//", "=%"]
follow["array_value"] = ["}"]
follow["array_value1"] = ["}"]
follow["more_array"] = ["}"]
follow["array_value2"] = ["}"]
follow["more_array2"] = ["}"]
follow["array_value3"] = ["}"]
follow["more_array3"] = ["}"]
follow["struct_dec"] = [";"]
follow["site_element"] = ["}"]
follow["more_element"] = ["}"]
follow["site_var"] = [";"]
follow["more_var_site"] = [";"]
follow["func_dec"] = [";"]
follow["func_type"] = ["id"]
follow["param"] = [")"]
follow["param1"] = [")"]
follow["local_dec"] = ["#",  "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                       "++", "--", "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["struct_init"] = [";"]
follow["more_struct"] = ["}"]
follow["statements"] = ["#", "kill", "revive"]
follow["statement1"] = ["#",  "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                        "++", "--", "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["expre_stmt"] = [";"]
follow["assign_expr"] = [";"]
follow["assign_op"] = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal", "neg_sheriff_literal",
                       "agent_literal", "roster_literal", "attack", "defend", "++", "--", "(", "and", "or", "n"]
follow["assign_operand"] = [";"]
follow["expre_stmt1"] = [";", ")"]
follow["arith_expr"] = [";", "+", "-", "*", "^", "/", "//",
                        "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow["arith_operand"] = [";", "+", "-", "*", "^", "/", "//",
                           "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow["num_val"] = [";", "+", "-", "*", "^", "/", "//",
                     "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow["una_expr"] = [";", "+", "-", "*", "^", "/", "//",
                      "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow["una_op"] = ["id", ";", "+", "-", "*", "^", "/", "//",
                    "%", ")", "==", "=!", "=>", "=<", ">", "<", ";", ","]
follow["arith_op"] = ["id", "classic_literal", "neg_classic_literal",
                      "sheriff_literal", "neg_sheriff_literal", "++", "--", "("]
follow["rela_expr"] = [";", ")", ","]
follow["rela_operand"] = ["==", "=!", "=>", "=<", ">", "<", ";", ")", ","]
follow["rela_op"] = ["id", "classic_literal", "neg_classic_literal",
                     "sheriff_literal", "neg_sheriff_literal", "++", "--", "("]
follow["log_expr"] = [";", ")", ","]
follow["log_expr1"] = [";", ")", ","]
follow["log_expr2"] = [";", ")", ","]
follow["log_op"] = [")"]
follow["log_operand"] = [",", ")"]
follow["ret_stmt"] = [";"]
follow["in_stmt"] = [";"]
follow["in_operand"] = [")"]
follow["out_stmt"] = [";"]
follow["out_operand"] = [")"]
follow["str_form"] = ["\""]
follow["str_var"] = ["roster_literal", "{", "\""]
follow["condi_stmt"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                        "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["if_stmt"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                     "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["condition"] = [")"]
follow["if_stmt1"] = ["else", "#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                      "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["if_stmt2"] = ["else", "#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                      "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["switch_stmt"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                         "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["case_literal"] = [":"]
follow["more_votes"] = ["base"]
follow["break"] = ["}"]
follow["loop_stmt"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                       "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["for_stmt"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                      "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["for_init"] = [";"]
follow["loop_cond"] = [";", ")"]
follow["break_con"] = ["}"]
follow["while_statement"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                             "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["dowhile_stmt"] = ["#", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                          "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
follow["function_def"] = ["#", "$"]

var = "#"


def first_set(var):
    # print(var)
    non_terminals = []
    for key, value in first.items():
        if var in value:
            non_terminals.append(key)
    return non_terminals


# CFG
cfg_program = ["comm", "global_dec", "comm", "bound",
               "{", "local_dec", "comm", "statement", "comm", "}", "comm", "function_def", "comm"]


tokens = ["classic", "const"]
for i in tokens:
    ctr = 0
    while True:
        if cfg_program[ctr] in first_set(i):
            print(cfg_program[ctr])
            print(ctr)
        ctr += 1
        if ctr >= len(cfg_program):
            break


# first_set("const")
