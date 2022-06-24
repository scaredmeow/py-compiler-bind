class GrammarRules:
    cfg = {}
    cfg["program"] = [["comm", "global_dec", "comm", "bound",
                      "{", "local_dec", "comm", "statements", "comm", "}", "comm", "function_def", "comm"]]
    cfg["comm"] = [["comment"]]
    cfg["comm"].append(["null"])
    cfg["global_dec"] = [["const_dec", ";", "global_dec"]]
    cfg["global_dec"].append(["var_dec", ";", "global_dec"])
    cfg["global_dec"].append(["array_dec", ";", "global_dec"])
    cfg["global_dec"].append(["struct_dec", ";", "global_dec"])
    cfg["global_dec"].append(["func_dec", ";", "global_dec"])
    cfg["global_dec"].append(["null"])
    cfg["const_dec"] = [["const", "data_type", "id", "=", "value", "const_dec1"]]
    cfg["const_dec1"] = [[",", "id", "=", "value", "const_dec1"]]
    cfg["const_dec1"].append(["null"])
    cfg["data_type"] = [["classic"]]
    cfg["data_type"].append(["sheriff"])
    cfg["data_type"].append(["agent"])
    cfg["data_type"].append(["roster"])
    cfg["data_type"].append(["map"])
    cfg["value"] = [["classic_literal"]]
    cfg["value"].append(["neg_classic_literal"])
    cfg["value"].append(["sheriff_literal"])
    cfg["value"].append(["neg_sheriff_literal"])
    cfg["value"].append(["agent_literal"])
    cfg["value"].append(["roster_literal"])
    cfg["value"].append(["roster_literal", "conc"])
    cfg["value"].append(["map_literal"])
    cfg["map_literal"] = [["attack"]]
    cfg["map_literal"].append(["defend"])
    cfg["conc"] = [["&", "roster_literal", "conc"]]
    cfg["conc"].append(["null"])
    cfg["var_dec"] = [["data_type", "id", "init", "var_dec1"]]
    cfg["init"] = [["=", "value"]]
    cfg["init"].append(["null"])
    cfg["var_dec1"] = [[",", "id", "init", "var_dec1"]]
    cfg["var_dec1"].append(["null"])
    cfg["array_dec"] = [["data_type", "arr", "[", "index", "]",
                        "array_index2", "array_index3", "id"]]
    cfg["array_dec"].append(["data_type", "arr", "[", "index", "]",
                             "array_index2", "array_index3", "id", "=", "{", "array_value", "}"])
    cfg["index"] = [["classic_literal"]]
    cfg["index"].append(["id"])
    cfg["index"].append(["func_stmt"])
    cfg["index"].append(["null"])
    cfg["func_stmt"] = ["id", "(", "args", ")"]
    cfg["args"] = [["variable", "more_args"]]
    cfg["args"].append(["value", "more_args"])
    cfg["args"].append(["null"])
    cfg["variable"] = [["id"]]
    cfg["variable"].append(["array_elem"])
    cfg["variable"].append(["struct_elem"])
    cfg["more_args"] = [[",", "variable", "more_args"]]
    cfg["more_args"].append([",", "value", "more_args"])
    cfg["more_args"].append(["null"])
    cfg["array_elem"] = [["id", "[", "index", "]", "array_index2", "array_index3"]]
    cfg["array_index2"] = [["[", "index", "]"]]
    cfg["array_index2"].append(["null"])
    cfg["array_index3"] = [["[", "index", "]"]]
    cfg["array_index3"].append(["null"])
    cfg["struct_elem"] = [["variable", ".", "variable"]]
    cfg["array_value"] = [["array_value1"]]
    cfg["array_value"].append(["array_value2"])
    cfg["array_value"].append(["array_value3"])
    cfg["array_value1"] = [["value", "more_array"]]
    cfg["more_array"] = [[",", "value", "more_array"]]
    cfg["more_array"].append(["null"])
    cfg["array_value2"] = [["{", "array_value1", "}", "more_array2"]]
    cfg["more_array2"] = [[",", "array_value2", "more_array2"]]
    cfg["more_array2"].append(["null"])
    cfg["array_value3"] = [["{", "array_value2", "}", "more_array3"]]
    cfg["more_array3"] = [[",", "array_value3", "more_array3"]]
    cfg["more_array3"].append(["null"])
    cfg["struct_dec"] = [["site", "id", "{", "site_element", "}", "site_var"]]
    cfg["site_element"] = [["var_dec", ";", "more_element"]]
    cfg["site_element"].append(["array_dec", ";", "more_element"])
    cfg["more_element"] = [["site_element"]]
    cfg["more_element"].append(["null"])
    cfg["site_var"] = [["id", "more_var_site"]]
    cfg["site_var"].append(["array_elem", "more_var_site"])
    cfg["site_var"].append(["null"])
    cfg["more_var_site"] = [[",", "id", "more_var_site"]]
    cfg["more_var_site"].append(["null"])
    cfg["func_dec"] = [["func_type", "id", "(", "param", ")"]]
    cfg["func_type"] = [["data_type"]]
    cfg["func_type"].append(["omen"])
    cfg["param"] = [["data_type", "id", "param1"]]
    cfg["param"].append(["null"])
    cfg["param1"] = [[",", "data_type", "id", "param1"]]
    cfg["param1"].append(["null"])
    cfg["local_dec"] = [["const_dec", ";", "local_dec"]]
    cfg["local_dec"].append(["var_dec", ";", "local_dec"])
    cfg["local_dec"].append(["array_dec", ";", "local_dec"])
    cfg["local_dec"].append(["struct_init", ";", "local_dec"])
    cfg["local_dec"].append(["null"])
    cfg["struct_init"] = [["site", "id", "id2",
                          "=", "{", "value", "more_struct", "}"]]
    cfg["struct_init"].append(["site", "id", "array_elem",
                               "=", "{", "value", "more_struct", "}"])
    cfg["more_struct"] = [[",", "value", "more_struct"]]
    cfg["more_struct"].append(["null"])
    cfg["statements"] = [["statement1", "statements"]]
    cfg["statements"].append(["null"])
    cfg["statement1"] = [["comm"]]
    cfg["statement1"].append(["local_dec"])
    cfg["statement1"].append(["expre_stmt", ";"])
    cfg["statement1"].append(["ret_stmt", ";"])
    cfg["statement1"].append(["in_stmt", ";"])
    cfg["statement1"].append(["out_stmt", ";"])
    cfg["statement1"].append(["condi_stmt"])
    cfg["statement1"].append(["loop_stmt"])
    cfg["statement1"].append(["func_stmt"])
    cfg["expre_stmt"] = [["assign_expr"]]
    cfg["expre_stmt"].append(["una_expr"])
    cfg["assign_expr"] = ["variable", "assign_op", "assign_operand"]
    cfg["assign_op"] = [["="]]
    cfg["assign_op"].append(["=+"])
    cfg["assign_op"].append(["=-"])
    cfg["assign_op"].append(["=*"])
    cfg["assign_op"].append(["=/"])
    cfg["assign_op"].append(["=^"])
    cfg["assign_op"].append(["=//"])
    cfg["assign_op"].append(["=%"])
    cfg["assign_operand"] = [["variable"]]
    cfg["assign_operand"].append(["value"])
    cfg["assign_operand"].append(["expre_stmt1"])
    cfg["assign_operand"].append(["func_stmt"])
    cfg["expre_stmt1"] = [["arith_expr"]]
    cfg["expre_stmt1"].append(["rela_expr"])
    cfg["expre_stmt1"].append(["log_expr"])
    cfg["expre_stmt1"].append(["una_expr"])
    cfg["arith_expr"] = [["arith_operand", "arith_op", "arith_operand"]]
    cfg["arith_operand"] = [["variable"]]
    cfg["arith_operand"].append(["num_val"])
    cfg["arith_operand"].append(["variable"])
    cfg["arith_operand"].append(["una_expr"])
    cfg["arith_operand"].append(["func_stmt"])
    cfg["arith_operand"].append(["arith_expr"])
    cfg["arith_operand"].append(["(", "arith_expr", ")"])
    cfg["num_val"] = [["classic_literal"]]
    cfg["num_val"].append(["neg_classic_literal"])
    cfg["num_val"].append(["sheriff_literal"])
    cfg["num_val"].append(["neg_sheriff_literal"])
    cfg["una_expr"] = [["una_op", "variable"]]
    cfg["una_expr"].append(["variable", "una_op"])
    cfg["una_op"] = [["++"]]
    cfg["una_op"].append(["--"])
    cfg["arith_op"] = [["+"]]
    cfg["arith_op"].append(["-"])
    cfg["arith_op"].append(["*"])
    cfg["arith_op"].append(["^"])
    cfg["arith_op"].append(["/"])
    cfg["arith_op"].append(["//"])
    cfg["arith_op"].append(["%"])
    cfg["rela_expr"] = [["rela_operand", "rela_op", "rela_operand"]]
    cfg["rela_operand"] = [["variable"]]
    cfg["rela_operand"].append(["num_val"])
    cfg["rela_operand"].append(["arith_expr"])
    cfg["rela_operand"].append(["una_expr"])
    cfg["rela_op"] = [["=="]]
    cfg["rela_op"].append(["=!"])
    cfg["rela_op"].append(["<"])
    cfg["rela_op"].append([">"])
    cfg["rela_op"].append(["=>"])
    cfg["rela_op"].append(["=<"])
    cfg["log_expr"] = [["log_expr1"]]
    cfg["log_expr"].append(["log_expr2"])
    cfg["log_expr1"] = [
        ["log_op", "(", "log_operand", ",", "log_operand", ")"]]
    cfg["log_expr2"] = [["n", "(", "log_operand", ")"]]
    cfg["log_op"] = [["and"]]
    cfg["log_op"].append(["or"])
    cfg["log_operand"] = [["log_expr"]]
    cfg["log_operand"].append(["rela_expr"])
    cfg["log_operand"].append(["map_literal"])
    cfg["log_operand"].append(["id"])
    cfg["ret_stmt"] = [["defuse", "ret_operand"]]
    cfg["ret_operand"] = [["id"]]
    cfg["ret_operand"].append(["value"])
    cfg["ret_operand"].append(["expr_stmt1"])
    cfg["in_stmt"] = [["aim", "(", "in_operand", ")"]]
    cfg["in_operand"] = [["variable"]]
    cfg["out_stmt"] = [["shoot", "(", "out_operand", ")"]]
    cfg["out_operand"] = [["variable"]]
    cfg["out_operand"].append(["roster_literal"])
    cfg["out_operand"].append(["func_stmt"])
    cfg["out_operand"].append(["expre_stmt1"])
    cfg["out_operand"].append(["fs", "\"", "str_form", "\""])
    cfg["str_form"] = [["srt_var", "roster_literal", "str_var", "str_form"]]
    cfg["str_form"].append(["null"])
    cfg["str_var"] = [["{", "id", "}"]]
    cfg["str_var"].append(["null"])
    cfg["condi_stmt"] = [["if_stmt"]]
    cfg["condi_stmt"].append(["switch_stmt"])
    cfg["if_stmt"] = [["if", "(", "condition", ")",
                      "{", "statements", "}", "if_stmt1", "if_stmt2"]]
    cfg["condition"] = [["map_literal"]]
    cfg["condition"].append(["rela_expr"])
    cfg["condition"].append(["log_expr"])
    cfg["if_stmt1"] = [["elif", "(", "condition",
                       "{", "statements", "}", "if_stmt1", "if_stmt2"]]
    cfg["if_stmt1"].append(["null"])
    cfg["if_stmt2"] = [["else", "{", "statements", "}"]]
    cfg["if_stmt2"].append(["null"])
    cfg["switch_stmt"] = [["switch", "(", "variable", ")", "{", "vote", "case_literal", ":", "statements",
                          "kill", ";", "more_votes", "base", ":", "statements", "break"]]
    cfg["case_literal"] = [["classic_literal"]]
    cfg["case_literal"].append(["agent_literal"])
    cfg["more_votes"] = [["vote", "case_literal", ":",
                         "statements", "kill", ";", "more_votes"]]
    cfg["more_votes"].append(["null"])
    cfg["break"] = [["kill", ";"]]
    cfg["break"].append(["null"])
    cfg["loop_stmt"] = [["for_stmt"]]
    cfg["loop_stmt"].append(["while_stmt"])
    cfg["loop_stmt"].append(["dowhile_stmt"])
    cfg["for_stmt"] = [["for", "(", "for_init", ";", "loop_cond",
                       ";", "una_expr", ")", "{", "statements", "break_con", "}"]]
    cfg["for_init"] = [["id", "=", "classic_literal"]]
    cfg["loop_cond"] = [["rela_expr"]]
    cfg["loop_cond"].append(["log_expr"])
    cfg["break_con"] = [["revive"]]
    cfg["break_con"].append(["kill"])
    cfg["break_con"].append(["null"])
    cfg["while_stmt"] = [["while", "(", "loop_cond", ")",
                         "{", "statements", "break_con", "}"]]
    cfg["dowhile_stmt"] = [[
        "do", "{", "statements", "break_con", "}", "while", "(", "loop_cond", ")", ";"]]
    cfg["function_def"] = [["plant", "func_type", "id",
                           "(", "param", ")", "{", "local_dec", "statements", "}"]]
    cfg["function_def"].append(["null"])
    non_terminal = list(cfg.keys())

    def __init__(self) -> None:
        self.cfg = GrammarRules.cfg
        self.non_terminal = GrammarRules.non_terminal


class FirstSet:
    first = {}
    first["comm"] = ["comment", "null"]
    first["global_dec"] = ["const", "classic", "sheriff",
                           "agent", "roster", "map", "site", "omen", "null"]
    first["const_dec"] = ["const"]
    first["const_dec1"] = [",", "null"]
    first["data_type"] = ["classic", "sheriff", "agent", "roster", "map"]
    first["value"] = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                      "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
    first["map_literal"] = ["attack", "defend"]
    first["conc"] = ["&", "null"]
    first["var_dec"] = ["classic", "sheriff", "agent", "roster", "map"]
    first["init"] = ["=", "null"]
    first["var_dec1"] = [",", "null"]
    first["array_dec"] = ["classic", "sheriff", "agent", "roster", "map"]
    first["index"] = ["classic_literal", "id", "null"]
    first["func_stmt"] = ["id"]
    first["args"] = ["id", "classic_literal", "neg_classic_literal", "sheriff_literal",
                     "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend", "null"]
    first["variable"] = ["id"]
    first["more_args"] = [",", "null"]
    first["array_elem"] = ["id"]
    first["array_index2"] = ["[", "null"]
    first["array_index3"] = ["[", "null"]
    first["struct_elem"] = ["id"]
    first["array_value"] = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                            "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend", "{"]
    first["array_value1"] = ["classic_literal", "neg_classic_literal", "sheriff_literal",
                             "neg_sheriff_literal", "agent_literal", "roster_literal", "attack", "defend"]
    first["more_array"] = [",", "null"]
    first["array_value2"] = ["{"]
    first["more_array2"] = [",", "null"]
    first["array_value3"] = ["{"]
    first["more_array3"] = [",", "null"]
    first["struct_dec"] = ["site"]
    first["site_element"] = ["classic", "sheriff", "agent", "roster", "map"]
    first["more_element"] = ["classic", "sheriff",
                             "agent", "roster", "map", "null"]
    first["site_var"] = ["id", "null"]
    first["more_var_site"] = [",", "null"]
    first["func_dec"] = ["classic", "sheriff",
                         "agent", "roster", "map", "omen"]
    first["func_type"] = ["classic", "sheriff",
                          "agent", "roster", "map", "omen"]
    first["param"] = ["classic", "sheriff", "agent", "roster", "map", "null"]
    first["param1"] = [",", "null"]
    first["local_dec"] = ["classic", "sheriff", "agent",
                          "roster", "map", "const", "site", "null"]
    first["struct_init"] = ["site"]
    first["more_struct"] = [",", "null"]
    first["statements"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id", "++", "--", "defuse",
                           "shoot", "if", "switch", "for", "while", "do", "null"]
    first["statement1"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id", "++", "--", "defuse",
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
    first["out_operand"] = ["id", "roster_literal", "classic_literal", "neg_classic_literal",
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

    def __init__(self) -> None:
        self.first = FirstSet.first

    def first_set(self, token, production) -> bool:
        try:
            if token in self.first[production]:
                return True
            return False
        except Exception as e:
            return False


class FollowSet:
    follow = {}
    follow["comm"] = ["const", "classic", "sheriff", "agent", "roster", "map", "site", "omen", "comment", "bound",  "id",  "++", '--',
                      "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "plant", "$", "kill", "revive"]
    follow["global_dec"] = ["comment", "bound"]
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
    follow["local_dec"] = ["comment",  "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                           "++", "--", "defuse", "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["struct_init"] = [";"]
    follow["more_struct"] = ["}"]
    follow["statements"] = ["comment", "kill", "revive"]
    follow["statement1"] = ["comment",  "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
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
    follow["condi_stmt"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                            "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["if_stmt"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                         "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["condition"] = [")"]
    follow["if_stmt1"] = ["else", "comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                          "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["if_stmt2"] = ["else", "comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                          "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["switch_stmt"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                             "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["case_literal"] = [":"]
    follow["more_votes"] = ["base"]
    follow["break"] = ["}"]
    follow["loop_stmt"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                           "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["for_stmt"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                          "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["for_init"] = [";"]
    follow["loop_cond"] = [";", ")"]
    follow["break_con"] = ["}"]
    follow["while_statement"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                                 "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["dowhile_stmt"] = ["comment", "const", "classic", "sheriff", "agent", "roster", "map", "site", "id",
                              "++", "--", 'defuse', "aim", "shoot", "if", "switch", "for", "while", "do", "}", "kill", "revive"]
    follow["function_def"] = ["comment", "$"]

    def __init__(self) -> None:
        self.follow = FollowSet.follow

    def follow_set(self, token, production) -> bool:
        try:
            if token in self.follow[production]:
                return True
            return False
        except Exception as e:
            return False


# def follow_set(token):
#     pass


# tokens = ["comment", "classic"]
# print(first_set("classic"))
# for i in tokens:
#     ctr = 0
#     while True:
#         if cfg["program[ctr] in first_set(i):
#             print(cfg["program[ctr])
#             print(ctr)
#         ctr += 1
#         if ctr >= len(cfg["program):
#             break


# print(FirstSet().first_set("bounda", "global_dec"))
