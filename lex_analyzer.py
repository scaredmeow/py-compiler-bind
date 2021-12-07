from typing import NamedTuple
import re

with open("rwords.txt") as f:
  rwords = f.read()
  rwords= list(item for item in rwords.split('\n') if item.strip())
with open("rsymbol.txt") as f:
  rsymbol = f.read()
  rsymbol = list(item for item in rsymbol.split('\n') if item.strip())  
class token(NamedTuple):
  type: str
  value: str
  line: int 
  lexpos: int
  errors: list

def tokenize(self):
  reserve_words = rwords
  reserve_symbol = rsymbol
  token_specification = [
    ('number',        r'!?\d+\.?\d*'),      # Integer or decimal number
    ('id',            r'[a-z][a-zA-Z_]*'),  # Identifiers
    ('char_literal',  r'\'[ -~]+'),        # Char          
    ('str_literal',   r'\"[ -~][ -~]+'),  # Str
    ('newline',       r'\n'),               # Line endings
    ('ignore',        r'[ \t]+'),          # Skip over spaces and tabs
    ('illegal',       r'.'),                # Any other character
  ]
  tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
  line_num = 1
  line_start = 0
  idno, idcount = 0,0
  errors = []
  idkey = {str:int}
  for mo in re.finditer(tok_regex, self):
    kind = mo.lastgroup
    value = mo.group()
    column = mo.start() - line_start
    if kind == 'number' and '.' not in value:       #Int
      if '!' in value and len(value) <= 10:         #Neg_int_literal
        kind = 'neg_int_literal'
        value = int(re.sub("!","-",value, 1))
      elif len(value) <= 9:                         #Int_literal
        kind = 'int_literal'
        value = int(value)
      else:                                         #Lex Error - Int_literal
        errors.append("Lexical Error (Ln {}, Col {}): Max digits for int literals is 9, you inputted {} digits".format(line_num,column,len(value)-1 if '!' in value else len(value)))
        kind = 'lex_error' 
    elif kind == 'number' and '.' in value:         #Deci
      length, i = 0,0
      while value[i] != '.':                        #Length Lefthandside
        length += 1
        i+=1
      if length <=10 and '!' in value and len(value) - length <=10:
        kind = 'neg_deci_literal'                   #Neg_deci_literal
        value = float(re.sub("!","-",value, 1))
      elif length <=9 and len(value) - length <=10:
        kind = 'deci_literal'                       #Deci_literal
        value = float(value)
      elif (length-1 if '!' in value else length) > 9 and len(value) - length <=10:
        errors.append("Lexical Error (Ln {}, Col {}): Max digits for left handside is 9, you inputted {} digits".format(line_num,column,length-1 if '!' in value else length))
        kind = 'lex_error'                          #Lex Error - Deci_literal - Left handside
      elif (length-1 if '!' in value else length) <= 9 and len(value) - length > 10:
        errors.append("Lexical Error (Ln {}, Col {}): Max digits for right handside is 9, you inputted {} digits".format(line_num,column,len(value) - length - 1))
        kind = 'lex_error'                          #Lex Error - Deci_literal - Right handside
      else:
        errors.append("Lexical Error (Ln {}, Col {}): Max digits for deci literals is 18, you inputted {} digits".format(line_num,column,len(value)-2 if '!' in value else len(value)-1))
        kind = 'lex_error'                          #Lex Error - Deci_literal
    elif kind == 'id' and value in reserve_words:   #Reserved Words
      kind = value
      if value == 'true' or value == 'false':
        kind = str(value) + ' and bool_literal'
    elif kind == 'char_literal':                    #Character
      if re.search(r'^\'[ -~]\'$',value):           #### FIX
        value = str(value[1])
      elif re.search(r'[ -&\(-~]$',value):
        kind = 'lex_error'
        errors.append("Lexical Error (Ln {}, Col {}): Char literal is unterminated".format(line_num,column))
      elif re.search(r'\'$',value):
        kind = 'lex_error'
        errors.append("Lexical Error (Ln {}, Col {}): Max characters for char literal is 1, you inputted {}".format(line_num,column,len(value)-2))
    elif kind == 'str_literal':                     #String
      value = str(value[1:len(value)-1]) 
    elif value in reserve_symbol:                   #Reserved Symnbols
      kind = value
    elif kind == 'id':                              #Identifier
      if len(value) > 15:
        errors.append("Lexical Error (Ln {}, Col {}): Max characters for identifiers is 15, you inputted {} characters".format(line_num,column,len(value)))
        kind = 'lex_error' 
      else:
        # idno+=1
        if value in idkey.keys():
          idno = idkey[value]
        else:
          idcount += 1
          idkey.update({value:idcount})
          idno = idkey[value]
    if kind == 'newline':                         #Newline  
      line_start = mo.end()
      line_num += 1
      continue
    elif kind == 'ignore':                          #Skip
      continue
    elif kind == 'illegal':                         #Mismatch
      errors.append("Lexical Error (Ln {}, Col {}): Illegal Character \"{}\" in {}".format(line_num,column,value,column))
      kind = 'lex_error' 
    yield token(kind+str(idno) if kind == 'id' else kind, value, line_num, column, errors)      #Tokenizer Output
  