import abc

class InputError( object ):
  def __init__( self, lineno, colno, char ):
    self.lineno, self.colno, self.char = lineno, colno, char

class LexicalAnalyser( metaclass = abc.ABCMeta ):

  @abc.abstractmethod
  def get_literals( self ):
    """return an array of literals"""
    return   
    
  @abc.abstractmethod
  def get_numbers( self ):
    """return an array of numbers"""
    return
    
  @abc.abstractmethod
  def get_reserved_words( self ):
    """return an array of reserved words"""
    return   
    
  @abc.abstractmethod
  def get_strings( self ):
    """return an array of strings"""
    return
 
  @abc.abstractmethod
  def get_variables( self ):
    """return an array of variables"""
    return   
 
  @abc.abstractmethod
  def get_bad_chars( self ):
    """return an array of InputError objects"""
    return   
