from table_judge import t_judge
from parameterized import parameterized


def judge_object(class_name):
  exec "from %(0)s import %(0)s; j = %(0)s()" % {"0": class_name}
  return j



class judge(parameterized):
  """Classifier base class."""
  
  
  def __init__(self):
    """@param idjudge is db:judge.id"""

    self.__idjudge = None
    self.flag_human = False
    self.lot = None # spectrum_lot object
    

  def judgement_object(self):
    """Returns a new judgement object. The class of this object is usually specific to the judge class."""
    return judgement()

  def set_idjudge(self, idjudge):
    self.__idjudge = idjudge
    
    
    if idjudge <> None:
      params = t_judge.get_value_from_id("params", idjudge)
      self.set_params(params)
        
   
  idjudge = property(lambda(self): self.__idjudge, set_idjudge)

  def get_description(self):
    """Class name is the default output of a judge when its description is asked for."""
    return self.__class__.__name__

  def get_explanation1(self):
    """Returns the range of possible values."""
    return ""


  def train(self):
    """Applies training algorithm in order to modify internal parameters. Abstract method."""
    output("Classifier %s does not have a training method." % str(self.__class__))
  
  def make_judgement(self):
    """Makes the self.judgement object."""
    pass

  def assure_uses_score(self):
    if not self.flag_uses_score:
      raise error_x("Classifier instance does not use score.", self)

  def set_idscore(self, value):
    self.assure_uses_score()
    self.score_index = self.idscore_s.index(value)

  #index = property(fget=lambda(self): self.__index, doc="Classification. Points to an element in idscore_s/codes.")
  idscore = property(fget=lambda(self): self.idscore_s[self.index], fset = set_idscore)
  
