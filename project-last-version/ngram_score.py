class ngram_score ( object ):

## NGRAM_SCORE is a class for the Ngram scoring program.

  def __init__( self, ngramfile, sep = ' ' ):
    ''' load a file containing ngrams and counts, calculate log probabilities '''

    import numpy as np

    self.ngrams = {}
    # open file in read mode
    file = open ( 'quadgrams.txt', 'r' )
    for line in file:
      key, count = line.split ( sep ) 
      self.ngrams[key] = int ( count )
    self.L = len ( key )
    self.N = sum ( self.ngrams.values() )

#  Calculate log probabilities.
#  If present apply the log10 of the probability
#  If not apply the 'pseudocounts' 

    for key in self.ngrams.keys():
      self.ngrams[key] = np.log10 ( float ( self.ngrams[key]) / self.N )
    self.floor = np.log10 ( 0.01 / self.N )

# Computing score of text
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