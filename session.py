import output
from table_experiment import t_experiment
from table_domain import t_domain
from table_deact import t_deact


SPECTRUM_COLORS_DEFAULT = ["#000000", "#f00000", "#00f000", "#0000f0", "#af00ad", "#e38b00", "#00585e", "#db3c70", "#72a76e", "#407675"];

class session_class(object):
  __idexperiment = -1 # 
  __iddomain = -1 # 
  __iddeact = -1 # 

  def __init__(self):
    self.spectrum_colors = SPECTRUM_COLORS_DEFAULT


  def show_selection(self, typename, id, name, comments):
    output.output("* %s %d: '%s' selected. " % (typename, id, name))
    if comments <> None and len(comments) > 0:
      output.output('  --- Comments: ---')
      output.output(comments)
      output.output('  -----------------')
    
  def set_idexperiment(self, idexperiment):
    self.__idexperiment = idexperiment
    row = t_experiment.get_values_from_id(("name", "comments"), self.__idexperiment)
    self.show_selection('Experiment', self.__idexperiment, row[0], row[1])   

  def set_iddomain(self, iddomain):
    self.__iddomain = iddomain
    row = t_domain.get_values_from_id(("name", "comments"), self.__iddomain)
    self.show_selection('Domain', self.__iddomain, row[0], row[1])

  def set_iddeact(self, iddeact):
    self.__iddeact = iddeact
    
    row = t_deact.get_values_from_id(("name", "comments"), self.__iddeact)
    self.show_selection('Activation scheme', self.__iddeact, row[0], row[1])

  
  def get_idexperiment(self):
    return self.__idexperiment

  def get_iddomain(self):
    return self.__iddomain

  def get_iddeact(self):
    return self.__iddeact
  
  idexperiment = property(get_idexperiment, set_idexperiment)
  iddomain = property(get_iddomain, set_iddomain)
  iddeact = property(get_iddeact, set_iddeact)
  
  
  def get_spectrum_color(self, i):
    return self.spectrum_colors[i % len(self.spectrum_colors)]
  
session = session_class()
  