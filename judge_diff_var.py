from judge_float import judge_float
import numpy

class judge_diff_var(judge_float):
  """Calculates the variance of the first difference vector"""
  
  def make_judgement(self):
    self.judgement = self.judgement_object()
    
    nn = self.lot.get_1spectrum(self.idspectrum)
    diff = numpy.diff(nn)
    
    self.judgement.value = diff.var() # nn is a numpy.array
    