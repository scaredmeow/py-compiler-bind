from typing import NamedTuple
import re, os

os.chdir('bind')                                                          # Getting tokens
with open("tokens/rwords.txt") as f:
  rwords = f.read()
  rwords= list(item for item in rwords.split('\n') if item.strip())
with open("tokens/rsymbol.txt") as f:
  rsymbol = f.read()
  rsymbol = list(item for item in rsymbol.split('\n') if item.strip())  

class Token(NamedTuple):
  type: str
  value: str
  line: int
  column: int
  error: list

def tokenize(code):
  keywords = rwords
  reserve_symbol = rsymbol
  token_specification = [
    ('number',        r'!?\d+\.?\d*'),                                    # Integer or decimal number
    ('id',            r'[a-z][a-zA-Z_]*'),                                # Identifiers
    # ('char_literal',  r'\'[ -~]+'),                                       # Char          
    # ('str_literal',   r'\"[ -~][ -~]+'),                                  # Str
    # ('symbols',       r'[ -~]+'),                                         # Symbols first 127 
    ('newline',       r'\n'),                                             # Line Terminate
    ('ignore',        r'[ \t]+'),                                         # Skip over spaces and tabs
    ('illegal',       r'.'),                                              # Any other character                                                                    # Variables
  ]
  tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
  line_num = 1
  line_start = 0
  idno, idcount = 0,0
  error = []
  idkey = {str:int}
  reIter = re.finditer(tok_regex, code)

  for mo in reIter:
      kind = mo.lastgroup
      value = mo.group()
      column = mo.start() - line_start
      if kind == 'number':
          value = float(value) if '.' in value else int(value)
      elif kind == 'id' and value in keywords:
          kind = value
      elif kind == 'newline':
          line_start = mo.end()
          line_num += 1
          continue
      elif kind == 'ignore':
          continue
      elif kind == 'illegal':
          error.append(f'{value!r} unexpected on line {line_num}')
          kind = 'lex-error'
      yield Token(kind, value, line_num, column, error)