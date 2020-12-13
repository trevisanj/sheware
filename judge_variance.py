from judge_float import judge_float

class judge_variance(judge_float):
  """Represents a random judge. This may be useful either as an example or as statistical tool."""
  
  def make_judgement(self):
    self.judgement = self.judgement_object()
    
    nn = self.lot.get_1spectrum(self.idspectrum)
    
    self.judgement.value = nn.var() # nn is a numpy.array
    