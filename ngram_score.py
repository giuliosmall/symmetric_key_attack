class ngram_score ( object ):

#*****************************************************************************80
#
## NGRAM_SCORE is a class for the Ngram scoring program.
#
#  Author:
#
#    Unknown
#
  def __init__( self, ngramfile, sep = ' ' ):
    ''' load a file containing ngrams and counts, calculate log probabilities '''

    import numpy as np

    self.ngrams = {}
    fh = open ( 'quadgrams.txt', 'rt' )
    for line in fh:
      key, count = line.split ( sep ) 
      self.ngrams[key] = int ( count )
    self.L = len ( key )
    self.N = sum ( self.ngrams.values() )
#
#  Calculate log probabilities.
#
    for key in self.ngrams.keys():
      self.ngrams[key] = np.log10 ( float ( self.ngrams[key]) / self.N )
    self.floor = np.log10 ( 0.01 / self.N )
  def score ( self, text ):
    ''' compute the score of text '''
    score = 0
    ngrams = self.ngrams.__getitem__
    for i in range ( len ( text ) - self.L + 1 ):
      if text[i:i+self.L] in self.ngrams: 
        score += ngrams ( text[i:i+self.L] )
      else:
        score += self.floor          
    return score