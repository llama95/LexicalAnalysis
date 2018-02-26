# to run this test, execute the command "python3 -m unittest -v <this file>"
import unittest, pprint
import lexer

test_input = '''
  vx = -123
  str = "abc"
  function ff_gg ( arg )
  begin
    return arg / 10 * ( vx + 4 )
  end
'''

class TestLexer( unittest.TestCase ):
  
  # setUp will be called by the test framework before every test
  def setUp ( self ):
    pass

  # setUp will be called by the test framework after every test
  def tearDown( self ):
    pass

  # each test must be self-contained and cannot depend on another
  # tests are executed in lexical order of their names
  
  def test_tokenization( self ):
    self.lx = lexer.Lexer( test_input )
    vars = self.lx.get_variables( )
    self.assertTrue( 'arg' in vars and 'ff_gg' in vars )
    self.assertEqual( len( vars ), 4 )
    
    lits = self.lx.get_literals( )
    self.assertTrue( '*' in lits and ')' in lits and '/' in lits )
    self.assertEqual( len( lits ), 6 )
    
    reserved = self.lx.get_reserved_words( )
    self.assertTrue( 'BEGIN' in reserved and 'END' in reserved )
    self.assertEqual( len( reserved ), 4 )
    
    self.assertEqual( len( self.lx.get_numbers( ) ), 3 )
    self.assertEqual( len( self.lx.get_strings( ) ), 1 )

  def test_bad_input( self ):
    # <, ? and : are not legal characters in our toy language
    self.lx = lexer.Lexer( " ( a < b ) ?  a : b " )
    bchars = self.lx.get_bad_chars( )
    self.assertEqual( len( bchars ), 3 )
    self.assertEqual( bchars[0].char, '<' )
    self.assertEqual( bchars[1].char, '?' )
    self.assertEqual( bchars[2].char, ':' )