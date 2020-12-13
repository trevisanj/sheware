from judge import judge
from judgement_float import judgement_float

class judge_float(judge):
  """Base class for judges which issue a float number, i.e., their judgement is a judgement_float object."""
  
  def judgement_object(self):
    return judgement_float()