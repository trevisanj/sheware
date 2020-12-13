from judge_float import judge_float
import math

class judge_data_density(judge_float):
  """Computes the data density of the spectrum in case.
  
  Formula taken from the Jemma & Plamen article of the mid 2008.
  
  D[z[k]] = 1/(1+1/(k-1)*sum(norm(z(k)-z(i))**2/2/sigma_2 for i until k-1)
  
  Note that there is no such 'k' in this implementation, because the spectrum in case is in nn and the other spetra are in oth.
  
  In fact, k-1 is len(oth)
  """
  
  def make_judgement(self):
    self.judgement = self.judgement_object()
    
    nn = self.lot.get_1spectrum(self.idspectrum)
    oth = self.lot.get_1colony(idspectrum=self.idspectrum, idspectrum_exclude=self.idspectrum, flag_active_only=True)
    
    if len(oth) > 0:
    
      # parameter
      sigma = 1
      sigma2 = sigma**2
      
      _sum = sum([sum((nn-nn2)**2) for nn2 in oth])

      D = 1./(1+1./len(oth)*_sum/2/sigma2)
      
    else:
      D = 1

    self.judgement.value = D
    