from judge_float import judge_float
import numpy

def sign(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  return 0

class judge_trend_shift(judge_float):
  """Calculates the number of trend shifts, i.e., how many times the derivative changed signal."""
  
  def make_judgement(self):
    self.judgement = self.judgement_object()
    
    nn = self.lot.get_1spectrum(self.idspectrum)
    diff = numpy.diff(nn)
    
    sig = 0
    count = 0
    for x in diff:
      sig_ = sign(x)
      if sig_ != sig:
        sig = sig_
        count += 1

    self.judgement.value = count
    