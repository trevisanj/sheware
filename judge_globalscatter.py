""" Pretty much like judge_distance, but this one calculates the 'global scatter' while the former calculater the 'colony scatter'"""
from judge_float import judge_float
import numpy as np
import math

class judge_globalscatter(judge_float):
  """Now working so isolated with an immediate "return". 
  Computes the average distance between the spectra which is the case and the other spectra from the colony."""

  flag_first = 1
  
  def make_judgement(self):
    if self.flag_first:
      self.judgement = self.judgement_object()

      self.oth = self.lot.all
      self.no_oth = len(self.oth)
      
      self.flag_first = 0

    nn = self.lot.get_1spectrum(self.idspectrum)
    
    d = 0
    no = len(nn)
    
    if self.no_oth > 0:
      for nn2 in self.oth:
        # qwe d += sum(abs(nn-nn2))
      
        # Computes the hyperhypotenuse length
        d += np.sum((nn-nn2)**2)
        

      d /= self.no_oth


    self.judgement.value = d
    