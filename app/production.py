# Backus Naur Form
# Program ::= comment

# global
# local
# statement

first = {}
follow = {}

# CFG
cfg_program = ["comm", "global_dec", "comm", "bound",
               "{", "local_dec", "comm", "statement", "comm", "}", "comm", "function_def", "comm"]
cfg_comm = ["#", "ascii"]
cfg_comm = ["null"]
cfg_global_dec = ["const_dec", ";", "global_dec"]
cfg_global_dec = ["var_dec", ";", "global_dec"]
cfg_global_dec = ["array_dec", ";", "global_dec"]
cfg_global_dec = ["struct_dec", ";", "global_dec"]
cfg_global_dec = ["func_dec", ";", "global_dec"]
cfg_global_dec = ["null"]
cfg_const_dec = ["const", "data_type", "id", "=", "value", "const_dec1"]
cfg_const_dec1 = [",", "id", "=", "value", "const_dec1"]
cfg_const_dec1 = ["null"]
cfg_data_type = ["classic"]
cfg_data_type = ["sheriff"]
cfg_data_type = ["agent"]
cfg_data_type = ["roster"]
cfg_data_type = ["map"]
cfg_value = ["classic_literal"]
cfg_value = ["neg_classic_literal"]
cfg_value = ["sheriff_literal"]
cfg_value = ["neg_sheriff_literal"]
cfg_value = ["agent_literal"]
cfg_value = ["roster_literal"]
cfg_value = ["roster_literal", "conc"]
cfg_value = ["map_literal"]
cfg_map_literal = ["attack"]
cfg_map_literal = ["defend"]
cfg_conc = ["&", "roster_literal", "conc"]
cfg_conc = ["null"]
cfg_var_dec = ["data_type", "id", "init", "var_dec1"]
cfg_var_dec1 = [",", "id", "init", "var_dec1"]
cfg_var_dec1 = ["null"]
cfg_array_dec = ["data_type", "arr", "[", "index", "]",
                 "array_index2", "array_index3", "id"]
cfg_array_dec = ["data_type", "arr", "[", "index", "]",
                 "array_index2", "array_index3", "id", "=", "{", "array_value", "}"]
cfg_index = ["classic_literal"]
cfg_index = ["id"]
cfg_index = ["func_stmt"]
cfg_index = ["null"]
cfg_func_stmt = ["id", "(", "args", ")"]
cfg_args = ["variable", "more_args"]
cfg_args = ["value", "more_args"]
cfg_args = ["null"]
cfg_variable = ["id"]
cfg_variable = ["array_elem"]
cfg_variable = ["struct_elem"]
cfg_more_args = [",", "variable", "more_args"]
cfg_more_args = [",", "value", "more_args"]
cfg_more_args = ["null"]
cfg_array_elem = ["id", "[", "index", "]", "array_index2", "array_index3"]
cfg_array_index2 = ["[", "index", "]"]
cfg_array_index2 = ["null"]
cfg_array_index3 = ["[", "index", "]"]
cfg_array_index3 = ["null"]
cfg_struct_elem = ["variable", ".", "variable"]
cfg_array_value = ["array_value1"]
cfg_array_value = ["array_value2"]
cfg_array_value = ["array_value3"]
cfg_array_value1 = ["value", "more_array"]
cfg_more_array = [",", "value", "more_array"]
cfg_more_array = ["null"]
cfg_array_value2 = ["{", "array_value1", "}", "more_array2"]
cfg_more_array2 = [",", "array_value2", "more_array2"]
cfg_more_array2 = ["null"]
cfg_array_value3 = ["{", "array_value2", "}", "more_array3"]
cfg_more_array3 = [",", "array_value3", "more_array3"]
cfg_more_array3 = ["null"]
cfg_struct_dec = ["site", "id", "{", "site_element", "}", "site_var"]
cfg_site_element = ["var_dec", ";", "more_element"]
cfg_site_element = ["array_dec", ";", "more_element"]
cfg_more_element = ["site_element"]
cfg_more_element = ["null"]
cfg_site_var = ["id", "more_var_site"]
cfg_site_var = ["array_elem", "more_var_site"]
cfg_site_var = ["null"]
cfg_more_var_site = [",", "id", "more_var_site"]
cfg_more_var_site = ["null"]
cfg_func_dec = ["func_type", "id", "(", "param", ")"]
cfg_funct_type = ["data_type"]
cfg_func_type = ["omen"]
cfg_param = ["data_type", "id", "param1"]
cfg_param = ["null"]
cfg_param1 = [",", "data_type", "id", "param1"]
cfg_param1 = ["null"]
cfg_local_dec = ["const_dec", ";", "local_dec"]
cfg_local_dec = ["var_dec", ";", "local_dec"]
cfg_local_dec = ["array_dec", ";", "local_dec"]
cfg_local_dec = ["struct_init", ";", "local_dec"]
cfg_local_dec = ["null"]
cfg_struct_init = ["site", "id", "id2", "=", "{", "value", "more_struct", "}"]
cfg_struct_init = ["site", "id", "array_elem",
                   "=", "{", "value", "more_struct", "}"]
cfg_more_struct = [",", "value", "more_struct"]
cfg_more_struct = ["null"]
cfg_statements = ["statement1", "statements"]
cfg_statements = ["null"]
cfg_statement1 = ["comm"]
cfg_statement1 = ["local_dec"]
cfg_statement1 = ["expre_stmt", ";"]
cfg_statement1 = ["ret_stmt", ";"]
cfg_statement1 = ["in_stmt", ";"]
cfg_statement1 = ["out_stmt", ";"]
cfg_statement1 = ["condi_stmt"]
cfg_statement1 = ["loop_stmt"]
cfg_statement1 = ["func_stmt"]
cfg_expre_stmt = ["assign_expr"]
cfg_expre_stmt = ["una_expr"]
cfg_assign_expr = ["variable", "assign_op", "assign_operand"]
cfg_assign_op = ["="]
cfg_assign_op = ["=+"]
cfg_assign_op = ["=-"]
cfg_assign_op = ["=*"]
cfg_assign_op = ["=/"]
cfg_assign_op = ["=^"]
cfg_assign_op = ["=//"]
cfg_assign_op = ["=%"]
cfg_assign_operand = ["variable"]
cfg_assign_operand = ["value"]
cfg_assign_operand = ["expre_stmt1"]
cfg_assign_operand = ["func_stmt"]
cfg_expre_stmt1 = ["arith_expr"]
cfg_expre_stmt1 = ["rela_expr"]
cfg_expre_stmt1 = ["log_expr"]
cfg_expre_stmt1 = ["una_expr"]
cfg_arith_expr = ["arith_operand", "arith_op", "arith_operand"]
cfg_arith_operand = ["variable"]
cfg_arith_operand = ["num_val"]
cfg_arith_operand = ["variable"]
cfg_arith_operand = ["una_expr"]
cfg_arith_operand = ["func_stmt"]
cfg_arith_operand = ["arith_expr"]
cfg_arith_operand = ["(", "arith_expr", ")"]
cfg_num_val = ["classic_literal"]
cfg_num_val = ["neg_classic_literal"]
cfg_num_val = ["sheriff_literal"]
cfg_num_val = ["neg_sheriff_literal"]
cfg_una_expr = ["una_op", "variable"]
cfg_una_expr = ["variable", "una_op"]
cfg_una_op = ["++"]
cfg_una_op = ["--"]
cfg_arith_op = ["+"]
cfg_arith_op = ["-"]
cfg_arith_op = ["*"]
cfg_arith_op = ["^"]
cfg_arith_op = ["/"]
cfg_arith_op = ["//"]
cfg_arith_op = ["%"]
cfg_rela_expr = ["rela_operand", "rela_op", "rela_operand"]
cfg_rela_operand = ["variable"]
cfg_rela_operand = ["num_val"]
cfg_rela_operand = ["arith_expr"]
cfg_rela_operand = ["una_expr"]
cfg_rela_op = ["=="]
cfg_rela_op = ["=!"]
cfg_rela_op = ["<"]
cfg_rela_op = [">"]
cfg_rela_op = ["=>"]
cfg_rela_op = ["=<"]
cfg_log_expr = ["log_expr1"]
cfg_log_expr = ["log_expr2"]
cfg_log_expr1 = ["log_op", "(", "log_operand", ",", "log_operand", ")"]
cfg_log_expr2 = ["n", "(", "log_operand", ")"]
cfg_log_op = ["and"]
cfg_log_op = ["or"]
cfg_log_operand = ["log_expr"]
cfg_log_operand = ["rela_expr"]
cfg_log_operand = ["map_literal"]
cfg_log_operand = ["id"]
cfg_ret_stmt = ["defuse", "ret_operand"]
cfg_ret_operand = ["id"]
cfg_ret_operand = ["value"]
cfg_ret_operand = ["expr_stmt1"]
cfg_in_stmt = ["aim", "(", "in_operand", ")"]
cfg_in_operand = ["variable"]
cfg_out_stmt = ["shoot", "(", "out_operand", ")"]
cfg_out_operand = ["variable"]
cfg_out_operand = ["\"", "roster_literal", "\""]
cfg_out_operand = ["func_stmt"]
cfg_out_operand = ["expre_stmt1"]
cfg_out_operand = ["fs", "\"", "str_form", "\""]
cfg_str_form = ["srt_var", "roster_literal", "str_var", "str_form"]
cfg_str_form = ["null"]
cfg_str_var = ["{", "id", "}"]
cfg_str_var = ["null"]
cfg_condi_stmt = ["if_stmt"]
cfg_condi_stmt = ["switch_stmt"]
cfg_if_stmt = ["if", "(", "condition", ")",
               "{", "statements", "}", "if_stmt1", "if_stmt2"]
cfg_condition = ["map_literal"]
cfg_condition = ["rela_expr"]
cfg_condition = ["log_expr"]
cfg_if_stmt1 = ["elif", "(", "condition",
                "{", "statements", "}", "if_stmt1", "if_stmt2"]
cfg_if_stmt1 = ["null"]
cfg_if_stmt2 = ["else", "{", "statements", "}"]
cfg_if_stmt2 = ["null"]
cfg_switch_stmt = ["switch", "(", "variable", ")", "{", "vote", "case_literal", ":", "statements",
                   "kill", ";", "more_votes", "base", ":", "statements", "break"]
cfg_case_literal = ["classic_literal"]
cfg_case_literal = ["agent_literal"]
cfg_more_votes = ["vote", "case_literal", ":",
                  "statements", "kill", ";", "more_votes"]
cfg_more_votes = ["null"]
cfg_break = ["kill", ";"]
cfg_break = ["null"]
cfg_loop_stmt = ["for_stmt"]
cfg_loop_stmt = ["while_stmt"]
cfg_loop_stmt = ["dowhile_stmt"]
cfg_for_stmt = ["for", "(", "for_init", ";", "loop_cond",
                ";", "una_expr", ")", "{", "statements", "break_con", "}"]
cfg_for_init = ["id", "=", "classic_literal"]
cfg_loop_cond = ["rela_expr"]
cfg_loop_cond = ["log_expr"]
cfg_break_con = ["revive"]
cfg_break_con = ["kill"]
cfg_break_con = ["null"]
cfg_while_stmt = ["while", "(", "loop_cond", ")",
                  "{", "statements", "break_con", "}"]
cfg_dowhile_stmt = [
    "do", "{", "statements", "break_con", "}", "while", "(", "loop_cond", ")", ";"]
cfg_function_def = ["plant", "func_type", "id",
                    "(", "param", ")", "{", "local_dec", "statements", "}"]
cfg_function_def = ["null"]


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
ctr = 0
while True:
    if cfg_program[ctr] in first_set("classic"):
        print(cfg_program[ctr])
        print(ctr)
    ctr += 1
    if ctr >= len(cfg_program):
        break


# first_set("const")
