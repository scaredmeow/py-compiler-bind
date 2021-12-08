import lex
class lexer:
  def __init__(self,expression):
    self.type = []
    self.value = []
    self.line = []
    self.column = []
    for token in lex.tokenize(expression):
      self.type.append(token.type)
      self.value.append(token.value)
      self.line.append(token.line)
      self.column.append(token.column)
    self.error = token.error

