#
import ply.lex as lex
import lexical_analyser

class Lexer(lexical_analyser.LexicalAnalyser):

    def __init__(self, s):
        self.orig_string = s
        self.toks = []      #array for our objs
        self.error_arr = [] #creates error array
        self.build()        #build
        self.test(s)        #calls test to tokenizer

    # List of token names
    tokens = (
       'NUMBER',
       'STRING',
       'RESERVED',
       'LITERALS',
       'VARIABLES'


    )
    #rules for tokens
    t_STRING = r'"([A-Za-z0-9_\./\\-]*)"'
    t_RESERVED = r'function|end|begin|return'
    t_LITERALS = '\*|\+|-|/|\(|\)|=|,|%'
    t_VARIABLES = r'[a-zA-Z_0-9]+'

    #action rule for numbers
    def t_NUMBER(self, t):
        r'\-?\d+'
        t.value = int(t.value)
        return t
    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        c = lexical_analyser.InputError(t.lineno, t.lexpos, t.value[0])
        self.error_arr.append(c)
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
            self.lexer = lex.lex(module=self, **kwargs)
    #test
    def test(self, data):
            self.lexer.input(data)
            while True:
                 tok = self.lexer.token()
                 if not tok:
                     break
                 self.toks.append(tok)
    def get_numbers(self, t):
        r'\-?\d+'
        t.value = int(t.value)
        return t

    #make a list of string types with their specific values added to a list one after another
    def get_strings(self):
        listStrings = [];
        if tok.type == STRING:
            listStrings.append(tok.value)
        return listStrings
    #make a list of reserved word types with their specific values added to a list one after another
    def get_reserved_words( self ):
      listResWords = [];
      for tok in self.toks:
          if tok.type == 'RESERVED':
              listResWords.append(tok.value)
      return   listResWords

    def get_literals( self ):
      listLiterals = [];
      for tok in self.toks:
          if tok.type == 'LITERALS':
              if tok.value not in listLiterals:
                  listLiterals.append(tok.value)
      return listLiterals
    #make a list of vars types with their specific values added to a list one after another
    def get_variables( self ):
      listVariables = []
      for tok in self.toks:
          if tok.type == 'VARIABLES' :
              if tok.value not in listVariables:
                  listVariables.append(tok.value)
      return listVariables

      #returns an array of input objs
    def get_bad_chars( self ):
          return self.error_arr
