from errors import *
from table_spectrum import t_spectrum
from table_series import t_series
from table_experiment import t_experiment
from table_domain import t_domain
import numpy
from output import *

class spectrum_lot(object):
  
  __idexperiment = -1
  __iddomain = -1
  __iddeact = -1
  __wncount = -1
  __flag_active_only = True
  __flag_read = False

  def set_idexperiment(self, value):
    self.__idexperiment = value

  def set_iddomain(self, value):
    self.__wncount = t_domain.get_value_from_id("wncount", value)
    print "oooooooooooooooooooooooooooooooooooooooo"
    print "set_iddomain("+str(value)+") with wncount = "+str(self.__wncount)
    self.__iddomain = value

  def set_iddeact(self, value):
    self.__iddeact = value


  idexperiment = property(fget=lambda(self): self.__idexperiment, fset=set_idexperiment)  
  iddomain = property(fget=lambda(self): self.__iddomain, fset=set_iddomain)
  iddeact = property(fget=lambda(self): self.__iddeact, fset=set_iddeact)
  
  wncount = property(fget=lambda(self):self.__wncount)
  
  def set_flag_active_only(self, value):
    self.__flag_active_only = value
  
  flag_active_only = property(fget=lambda(self): self.__flag_active_only, fset=set_flag_active_only)

  def assure_experiment(self):
    if self.__idexperiment <= 0:
      raise error_x("Experiment not assigned!", self)

  def read(self):
    self.assure_experiment()
    
    output("Reading spectrum lot...")
#    try:
    output("  Doing the big SQL select...")
    
    # The "X" matrix
    data = t_spectrum.get_cursor_data(("spectrum.id", "idcolony", "series.vector", "flag_inactive"), idexperiment=self.idexperiment, 
       iddomain=self.iddomain, iddeact=self.iddeact, flag_active_only=self.flag_active_only).fetchall()
    output("  ...ok")
    no_rows = len(data)
    self.data = data
    self.no_rows = no_rows
    
    
    # Will mount dictionaries to make possible to find spectra by idcolony or idspectrum.
    # No need to sort by_colony because data1 comes there is an "order by colony.code" in the SQL statement int table_spectrum
    by_colony = {}
    by_spectrum = {}
    by_index = {}
    self.by_colony = by_colony
    self.by_spectrum = by_spectrum
    self.by_index = by_index
    
    # Will mount also the actual spectrum data
    all = numpy.zeros((no_rows, self.__wncount))  
    self.all = all



    # There is no sense in showing progress because the part which takes more time is the data_huge select, which is not progress-inspectable!
    output("  Organizing...")
    i = 0
    i_data = 0
    idcolony_now = -1
    for (idspectrum, idcolony, vector, flag_inactive) in self.data:
      
      if type(vector) == str:
      
        if idcolony <> idcolony_now:
          idcolony_now = idcolony
          try:
              # data1 comes sorted by db:colony.code, but for some explainable reason idcolony is not sorted accordingly,
            # i.e., the same idcolony appears again, i.e., it may alternate.
            test = by_colony[idcolony]
          except:
            by_colony[idcolony] = []
          
        by_colony[idcolony].append((i, idspectrum, not flag_inactive))
        by_spectrum[idspectrum] = (i, idcolony, not flag_inactive)
        by_index[i] = (idspectrum, idcolony)
        
        all[i, :] = str2vector(vector)
        
        i += 1
      
    output("  ...ok")
    output("...done!")
#    except Exception, e:
#      output("...failed!")
#      raise e
  
  def get_idspectrum_s(self):
    return self.by_spectrum.keys()

  def get_idcolony_s(self):
    return self.by_colony.keys()
      
  def get_1spectrum(self, idspectrum):
    return self.all[self.by_spectrum[idspectrum][0]]
      
  def get_1colony(self, idcolony=None, idspectrum=None, idspectrum_exclude = None, flag_active_only=False):
    
    assert(idcolony or idspectrum)
    
    if idspectrum:
      idcolony = self.by_spectrum[idspectrum][1]
    
    flag_exclude = idspectrum_exclude and True or False
    
    colony_list = self.by_colony[idcolony]
    number_rows = len(colony_list)
      
    # Checks if idspectrum_exclude is really in the list
    # And also how many inactive spectra will be excludad
    flag_is = False
    for x in colony_list:
      if flag_exclude and x[1] == idspectrum_exclude:
        flag_is = True
        number_rows -= 1
      elif flag_active_only and x[2] == 0:
        number_rows -= 1
          
    if flag_exclude and not flag_is:
      print idspectrum
      print colony_list
      raise error_x("I was told to exclude spectrum %s, but it is not in the list!" % (idspectrum_exclude,))
        
    
    result = numpy.zeros((number_rows, self.__wncount))
    
    i = 0
    for x in colony_list:
      if (not flag_active_only or x[2] == 1) and (not flag_exclude or x[1] <> idspectrum_exclude):
        result[i] = self.all[x[0]]
        i += 1
        
    return result
      
    
      

