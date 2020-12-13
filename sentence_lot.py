from table_judge import t_judge
from table_spectrum import t_spectrum
from table_series import t_series
from table_experiment import t_experiment
from judge import *
import numpy
from output import *

class sentence_lot(object):
  """This class should be no longer used. Use table_spectrum.get_cursor_data() once you know what data you need.
  Maybe modify spectrum_lot class to aggregate the "sentences"  """
  
  __idexperiment = -1
  __idjudge = -1
  __flag_active_only = True
  
  colors = ["#000000"]
  
  def set_idjudge(self, value):
    self.__idjudge = value

  idjudge = property(fget=lambda(self): self.__idjudge, fset=set_idjudge)
  
  def set_flag_active_only(self, value):
    self.__flag_active_only = value
  
  flag_active_only = property(fget=lambda(self): self.__flag_active_only, fset=set_flag_active_only)


  def set_idexperiment(self, value):
    self.__wncount = t_experiment.get_value_from_id("wncount", value)
    self.__idexperiment = value

  idexperiment = property(fget=lambda(self): self.__idexperiment, fset=set_idexperiment)  


  def read(self):
    # data contains tuples ((idspectrum, params), ...
    self.data = t_spectrum.get_cursor_data(field_names=("spectrum.id",), idjudge_s=(self.idjudge,), idexperiment=self.idexperiment, 
    iddeact=self.iddeact, flag_active_only=self.flag_active_only).fetchall()


  def calculate(self):

    jg = judge_object(t_judge.get_value_from_id("class_name", self.idjudge))
    jm = jg.judgement_object()
  
    values = []
    self.values = values
    
    value_indexes = []
    self.value_indexes = value_indexes

    possible_values = []
    self.possible_values = possible_values

    i = 0
    for row in self.data:
      jm.set_params(row[1])
      
      value = jm.get_default_value()
      values.append(value)
      
      try:
        index = possible_values.index(value)
      except:
        possible_values.append(value)
        index = len(possible_values)-1
      
      value_indexes.append(index)


  def get_color(self, index):
    return self.colors[self.value_indexes[index] % len(self.colors)]    
      

  def get_colors(self):
    colors = []
    no_colors = len(self.colors)
    for value_index in self.value_indexes:
      colors.append(self.colors[value_index % no_colors])
    return colors
  