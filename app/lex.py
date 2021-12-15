from typing import NamedTuple
import re, os

#----------------------------------------------------------------------------------------------------------
os.chdir('app')                                                           # Getting tokens
with open("tokens/rword.txt") as f:
  rwords = f.read()
  rwords= list(item for item in rwords.split('\n') if item.strip())
with open("tokens/rsymbol.txt") as f:
  rsymbol = f.read()
  rsymbol = list(item for item in rsymbol.split('\n') if item.strip())  
#----------------------------------------------------------------------------------------------------------
class Token(NamedTuple):
  type: str
  value: str
  line: int
  column: int
  error: str
#----------------------------------------------------------------------------------------------------------
def tokenize(code):
  keywords = rwords
  reserve_symbol = rsymbol
  token_specification = [
    ('number',        r'!?\d+\.?\d*'),                                     # Integer or decimal number
    ('id',            r'[a-z][0-9a-zA-Z_]*'),                                # Identifiers
    ('char_literal',  r'\'[ -&\(-~]+\'?'),                                       # Char          (\\\\)(\\\')(\\\")(\\\?) 
    ('str_literal',   r'\"[ -!#-~]+\"?'),                                  # Str
    ('symbols',       r'[%-&\(-\-\/:-\?\[\]\^\{\}]+'),                                         # Symbols first 127 
    ('comment',       r'#[ -~]+'),
    # ('separator'      r''),
    ('newline',       r'\n'),                                             # Line Terminate
    ('escseq', r'(\\a)|(\\b)|(\\f)|(\\n)|(\\r)|(\\t)|(\\v)|(\\\\)|(\\\')|(\\\")|(\\\?)|(\\0)'),
    ('whitespace',    r'[ \t]+'),                                         # Skip over spaces and tabs
    ('illegal',       r'.'),                                              # Any other character                                                                    # Variables
  ]
  tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
  line_num = 1
  line_start = 0
  idno, idcount = 0,0
  error = ""
  idkey = {str:int}
  reIter = re.finditer(tok_regex, code)
#----------------------------------------------------------------------------------------------------------
  for mo in reIter:
    kind = mo.lastgroup
    value = mo.group()
    column = mo.start() - line_start
#----------------------------------------------------------------------------------------------------------  
    if kind == 'id' and value in keywords:
      kind = value
#----------------------------------------------------------------------------------------------------------
    elif kind =='symbols':                                         # Reserved Symnbols
      if value in reserve_symbol: kind = value
      else: 
        kind = 'illegal'
        error = (f'Lexical Error on Ln {line_num}, Col {column}: Unexpected Illegal Character {value!r}')
        kind = 'lex-error'
#----------------------------------------------------------------------------------------------------------
    elif kind == 'id':                                                    # Identifier
      if len(value) > 15:
        error = (f'Lexical Error on Ln {line_num}, Col {column}: Identifier exceeded a max length of 15 \ncharacters, you inputted {len(value)} characters')
        kind = 'lex-error' 
      else:
        if value in idkey.keys():
          idno = idkey[value]
        else:
          idcount += 1
          idkey.update({value:idcount})
          idno = idkey[value]
#----------------------------------------------------------------------------------------------------------
    elif kind == 'char_literal':                                          # Character
      if re.search(r'(\'\\\'\')|(\'[ -&\(-\[\]-~]\'$)',value):                                 # FIX
        # if re.search(r'\'[ -&\(-\[\]-~]\'',value):value = str(value[1])  
        # else: value = str(value[2]) 
        pass
      elif re.search(r'[ -&\(-~]$',value):
        kind = 'lex-error'
        error = (f'Lexical Error Ln {line_num}, Col {column}): Char literal is unterminated')
      elif re.search(r'\'$',value):
        kind = 'lex-error'
        error = (f'Lexical Error Ln {line_num}, Col {column}: Char literal exceeded a max length of 1, you inputted {len(value)-2} character/s')
#----------------------------------------------------------------------------------------------------------
    elif kind == 'str_literal':                                     # String
      if (len(value)-2 > 1 if re.search(r'\"$',value) else len(value)-1 > 1):
        if re.search(r'(\"[ -!#-\[\]-~]*?(\\\")+?[ -!#-\[\]-~]*?\"$)|(\"[ -!#-\[\]-~][ -!#-\[\]-~]+?\"$)',value):                                 # FIX
          # if re.search(r'\"[ -!#-\[\]-~]*(\\\")+[ -!#-\[\]-~]*\"',value): 
          #   value = value.replace("\\\"","\"")
          # value = str(value[1:len(value)-1])
          pass
        elif re.search(r'[ -!#-~]$',value):
          kind = 'lex-error'
          error = (f'Lexical Error Ln {line_num}, Col {column}): String literal is unterminated')
      else:
        kind = 'lex-error'
        error = (f'Lexical Error Ln {line_num}, Col {column}: Str literal minimum character length is \n2 characters, you inputted {len(value)-2} character')                                
#----------------------------------------------------------------------------------------------------------  
    elif kind == 'number' and '.' not in value:                           # Int
      if '!' in value and len(value) <= 10:                               # Neg_int_literal
        kind = 'neg_int_literal'
        if re.search(r'^(!0+)$',value):
          error = (f'Lexical Error on Ln {line_num}, Col {column}: Negative Zero Error')
          kind = 'lex-error' 
        else:
          value = int(re.sub("!","-",value, 1))
      elif len(value) <= 9:                                               # Int_literal
        kind = 'int_literal'
        value = int(value)
      else:                                                               # Lex Error - Int_literal
        error = (f'Lexical Error on Ln {line_num}, Col {column}: Int literals exceeded a max length of 9, \nyou inputted {len(value)-1 if "!" in value else len(value)} digits')
        kind = 'lex-error' 
#----------------------------------------------------------------------------------------------------------    
    elif kind == 'number' and '.' in value:                               # Deci
      length, i = 0,0
      while value[i] != '.':                                              # Length Lefthandside
        length += 1
        i+=1
      if length <=10 and '!' in value and len(value) - length <=10:
        kind = 'neg_deci_literal'        
        if re.search(r'^((!0+).??0*?)$',value):
          error = (f'Lexical Error on Ln {line_num}, Col {column}: Negative Zero Error')
          kind = 'lex-error'    
        else:                              # Neg_deci_literal
          value = float(re.sub("!","-",value, 1))
      elif length <=10 and '!' in value and len(value) - length <=10 and re.search(r'^(!0+)$',value):
        error = (f'Lexical Error on Ln {line_num}, Col {column}: Negative Zero Error')
        kind = 'lex-error'
      elif length <=9 and len(value) - length <=10:
        kind = 'deci_literal'                                             # Deci_literal
        value = float(value)
      elif (length-1 if '!' in value else length) > 9 and len(value) - length <=10:
        error = (f'Lexical Error on Ln {line_num}, Col {column}: Deci literals exceeded in left handside \na max length of 9, you inputted {length-1 if "!" in value else length} digits')
        kind = 'lex-error'                                                # Lex Error - Deci_literal - Left handside
      elif (length-1 if '!' in value else length) <= 9 and len(value) - length > 10:
        error = (f'Lexical Error on Ln {line_num}, Col {column}: Deci literals exceeded in right handside \na max length of 9, you inputted {len(value) - length - 1} digits')
        kind = 'lex-error'                                                # Lex Error - Deci_literal - Right handside
      else:
        error = (f'Lexical Error on Ln {line_num}, Col {column}: Deci literals exceeded a max length of 18,\nyou inputted {len(value)-2 if "1" in value else len(value)-1} digits')
        kind = 'lex-error'                                                # Lex Error - Deci_literal
#----------------------------------------------------------------------------------------------------------             
    elif kind == 'newline':
      line_start = mo.end()
      line_num += 1
#----------------------------------------------------------------------------------------------------------
    elif kind == 'illegal':
      error = (f'Lexical Error on Ln {line_num}, Col {column}: Unexpected Illegal Character {value!r}')
      kind = 'lex-error'
#---------------------------------------------------------------------------------------------------------- 
    yield Token(kind+str(idno) if kind == 'id' else kind, value, line_num, column, error)