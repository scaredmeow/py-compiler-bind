import lex
import os
deli_reserved = {"sep(:)": ["base"], "open_array": [
    "arr"], "array_delim": ["]"]}
# ----------------------------------------------------------------------------------------------------------
# os.chdir('app')                                                           # Getting tokens
with open("tokens/rword.txt") as f:
    rwords = f.read()
    rwords = list(item for item in rwords.split('\n') if item.strip())
with open("tokens/rsymbol.txt") as f:
    rsymbol = f.read()
    rsymbol = list(item for item in rsymbol.split('\n') if item.strip())
with open("tokens/rdef/whitespace.txt") as f:
    whitespace = f.read()
    whitespace = list(item for item in whitespace.split('\n') if item.strip())
with open("tokens/rdef/open_func.txt") as f:
    open_func = f.read()
    open_func = list(item for item in open_func.split('\n') if item.strip())
with open("tokens/rdef/open_codeBlock.txt") as f:
    open_codeBlock = f.read()
    open_codeBlock = list(
        item for item in open_codeBlock.split('\n') if item.strip())
with open("tokens/rdef/line_delim.txt") as f:
    line_delim = f.read()
    line_delim = list(item for item in line_delim.split('\n') if item.strip())
with open("tokens/rdef/expr_delim.txt") as f:
    expr_delim = f.read()
    expr_delim = list(item for item in expr_delim.split('\n') if item.strip())
with open("tokens/rdef/id_rdef.txt") as f:
    id_rdef = f.read()
    id_rdef = list(item for item in id_rdef.split('\n') if item.strip())
with open("tokens/rdef/alphanumeric.txt") as f:
    alphanumeric = f.read()
    alphanumeric = list(
        item for item in alphanumeric.split('\n') if item.strip())
deli_reserved["whitespace"] = whitespace
deli_reserved["open_func"] = open_func
deli_reserved["open_codeBlock"] = open_codeBlock
deli_reserved["line_delim"] = line_delim
deli_reserved["expr_delim"] = expr_delim
deli_reserved["id_rdef"] = id_rdef
# ----------------------------------------------------------------------------------------------------------


class lexer:
    def __init__(self, expression):
        tmptype = []
        tmpvalue = []
        tmpline = []
        tmpcolumn = []
        tmperror = []

        for token in lex.tokenize(expression):
            tmptype.append(token.type)
            tmpvalue.append(token.value)
            tmpline.append(token.line)
            tmpcolumn.append(token.column)
            tmperror.append(token.error)

        rdefinition = {"whitespace": [" ", "\t"], "open_codeBlock": ["{"], "open_array": ["["], "open_func": ["("],
                       "close_block": [")", "]", "}"], "sep(:)": [":"], "line_delim": ["\n"], "arith_op": ["+", "-", "*", "/", "%", "!"],
                       "rela_op": [">", "<", "==", "=!", "=>", "=>", "=<"], "comb_op": ["=-", "=*", "=/", "=%", "=+"],
                       "logi_op": ["and", "or", "n"], "una_op": ["++", "--"], "separator": [",", "&"], "terminator": [";"]}
        rdefinition["whitespace"] += rdefinition["line_delim"]
        rdefinition["array_delim"] = rdefinition["comb_op"] + rdefinition["open_array"] + \
            rdefinition["close_block"] + rdefinition["whitespace"]
        rdefinition["id_rdef"] = alphanumeric + rdefinition["whitespace"] + \
            ["_", "\""] + rdefinition["close_block"]
        rdefinition["expr_delim"] = rdefinition["una_op"] + \
            rdefinition["id_rdef"] + ["!", ","]
        rdefinition["operator"] = rdefinition["arith_op"] + \
            rdefinition["rela_op"] + \
            rdefinition["comb_op"] + rdefinition["una_op"]
        rdefinition["num_delim"] = (rdefinition["whitespace"] + rdefinition["open_func"] + rdefinition["operator"]
                                    + rdefinition["close_block"] + rdefinition["separator"] + rdefinition["line_delim"])
        rdefinition["id_delim"] = rdefinition["num_delim"] + \
            rdefinition["open_array"] + rdefinition["terminator"]
        rdefinition["open_codeBlock"] += rdefinition["whitespace"]
        rdefinition["open_array"] += rdefinition["whitespace"]
        rdefinition["open_func"] += rdefinition["whitespace"]

        rdefinition["separator"] += rdefinition["whitespace"] + \
            rdefinition["terminator"]

        self.type = []
        self.value = []
        self.line = []
        self.column = []
        self.error = []

        for i in range(len(tmpvalue)):
            if i+1 == len(tmpvalue):
                self.type.append(tmptype[i])
                self.value.append(tmpvalue[i])
                self.error.append(tmperror[i])
                break
            if ((tmpvalue[i] in rdefinition["whitespace"]) or tmptype == "newline"):
                continue
            if tmptype[i] in rwords or tmptype[i] in rsymbol or tmptype[i] == "comment":
                if tmpvalue[i] == 'fs':
                    if tmptype[i+1] == "str_literal":
                        self.type.append(tmptype[i])
                        self.value.append(tmpvalue[i])
                        self.error.append(tmperror[i])
                    else:
                        self.type.append('lex-error')
                        self.value.append(tmpvalue[i])
                        self.error.append(
                            f'Lexical Error on Ln {tmpline[i]}, Col {tmpcolumn[i]}: "{tmpvalue[i+1]}" is not a valid delimiter for {tmptype[i]} ')
                        break
                else:
                    for j, k in deli_reserved.items():
                        if tmpvalue[i] in k:
                            if str(tmpvalue[i+1]) in rdefinition[j] or (True if tmptype[i+1] == ("str_literal" or "char_literal") or tmptype[i+1][0:2] == "id" else False):
                                self.type.append(tmptype[i])
                                self.value.append(tmpvalue[i])
                                self.error.append(tmperror[i])
                            else:
                                self.type.append('lex-error')
                                self.value.append(tmpvalue[i])
                                self.error.append(
                                    f'Lexical Error on Ln {tmpline[i]}, Col {tmpcolumn[i]}: "{tmpvalue[i+1]}" is not a valid delimiter for {tmptype[i]} ')
                                break
                        else:
                            continue
            elif tmptype[i][0:2] == "id":
                if tmpvalue[i+1] in rdefinition["id_delim"]:
                    self.type.append(tmptype[i])
                    self.value.append(tmpvalue[i])
                    self.error.append(tmperror[i])
                else:
                    self.type.append('lex-error')
                    self.value.append(tmpvalue[i])
                    self.error.append(
                        f'Lexical Error on Ln {tmpline[i]}, Col {tmpcolumn[i]}: "{tmpvalue[i+1]}" is not a valid delimiter for {tmptype[i]} ')
                    break
            elif tmptype[i] == "str_literal" or tmptype[i] == "char_literal":
                if tmpvalue[i+1] in rdefinition["id_delim"]:
                    self.type.append(tmptype[i])
                    self.value.append(tmpvalue[i])
                    self.error.append(tmperror[i])
                else:
                    self.type.append('lex-error')
                    self.value.append(tmpvalue[i])
                    self.error.append(
                        f'Lexical Error on Ln {tmpline[i]}, Col {tmpcolumn[i]}: "{tmpvalue[i+1]}" is not a valid delimiter for {tmptype[i]} ')
                    break
            elif tmptype[i] == "int_literal" or tmptype[i] == "deci_literal" or tmptype[i] == "neg_int_literal" or tmptype[i] == "neg_deci_literal":
                if tmpvalue[i+1] in rdefinition["id_delim"]:
                    self.type.append(tmptype[i])
                    self.value.append(tmpvalue[i])
                    self.error.append(tmperror[i])
                else:
                    self.type.append('lex-error')
                    self.value.append(tmpvalue[i])
                    self.error.append(
                        f'Lexical Error on Ln {tmpline[i]}, Col {tmpcolumn[i]}: "{tmpvalue[i+1]}" is not a valid delimiter for {tmptype[i]} ')
                    break
            else:
                self.type.append(tmptype[i])
                self.value.append(tmpvalue[i])
                self.error.append(tmperror[i])
                continue
