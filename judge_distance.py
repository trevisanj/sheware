from judge_float import judge_float
import math

class judge_distance(judge_float):
  """Computes the average distance between the spectra which is the case and the other spectra from the colony."""
  
  def make_judgement(self):
    self.judgement = self.judgement_object()
    
    nn = self.lot.get_1spectrum(self.idspectrum)
    oth = self.lot.get_1colony(idspectrum=self.idspectrum, idspectrum_exclude=self.idspectrum)
    
    d = 0
    no = len(nn)
    
    if len(oth) > 0:
      for nn2 in oth:
        # qwe d += sum(abs(nn-nn2))
      
        # Computes the hyperhypotenuse length
        d += sum((nn-nn2)**2)

      d /= len(oth)
    
    self.judgement.value = d
    