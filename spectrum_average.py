"""Not working properly"""
from errors import *
from table_spectrum import t_spectrum
from table_series import t_series
from table_experiment import t_experiment
import numpy as np
from output import *

class spectrum_average(object):
  """Takes a spectrum_lot object as parameter and averages the spectra by colony."""
  
  __idexperiment = -1
  __wncount = -1
  __spectrum_lot = None
  __flag_calculated = False
  __all = None
  __comments = None
  __by_colony = None
  __by_index = None

  def set_idexperiment(self, value):
    self.__wncount = t_experiment.get_value_from_id("wncount", value)
    self.__idexperiment = value

  idexperiment = property(fget=lambda(self): self.__idexperiment, fset=set_idexperiment)  
  wncount = property(fget=lambda(self):self.__wncount)

  all = property(fget=lambda(self): self.__all)
  comments = property(fget=lambda(self): self.__comments)
  by_colony = property(fget=lambda(self): self.__by_colony)
  by_index = property(fget=lambda(self): self.__by_index)

  def set_spectrum_lot(self, value):
    self.__spectrum_lot = value
    self.__flag_calculated = False

  spectrum_lot = property(fget=lambda(self): self.__spectrum_lot, fset=set_spectrum_lot)  


  def assure_spectrum_lot(self):
    if self.__spectrum_lot == None:
      raise error_x("Spectrum_lot not assigned!")

  def calculate(self):
    self.assure_spectrum_lot()
    
    output("Averaging...")
    sl = self.__spectrum_lot
    no = len(sl.all)

    # Indexes
    by_colony = {} # elements will be idcolony: index
    by_index = {} # elements will be index: idcolony
    self.__by_colony = by_colony
    self.__by_index = by_index
    
    # Initializes the spectrum data (in the case, averages)
    all = numpy.zeros((no, sl.wncount))  
    self.__all = all
    comments = []
    self.__comments = comments


    i = 0
    ii = 0
    idcolony_s = sl.get_idcolony_s()
    for idcolony in idcolony_s:
      curves = sl.get_1colony(idcolony)
      all[i] = np.mean(curves, 0) # takes the mean along the x/column axis, i.e., averages by wavenumber
      
      by_colony[idcolony] = i
      by_index[i] = idcolony
      
      comments.append("Averaged from %s spectr[um/a]" % str(len(curves)).rjust(3, "0"))
        
      i += 1
      
      ii += 1
      if ii == 100:
        ii = 0
        progress(float(i+1)/no)
    
    output("...done!")
  
  def get_1colony(self, idcolony):
    return self.all[self.by_colony[idcolony]]
    
      
