from judge_float import judge_float
import numpy

class judge_diff2_var(judge_float):
  """Calculates the variance of the second difference vector"""
  
  def make_judgement(self):
    self.judgement = self.judgement_object()
    
    nn = self.lot.get_1spectrum(self.idspectrum)
    diff2 = numpy.diff(nn, 2)
    
    self.judgement.value = diff2.var() # nn is a numpy.array
    