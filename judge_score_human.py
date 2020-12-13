from judge_score import judge_score
from errors import *

class judge_score_human(judge_score):
  """Represents a human who assigns a score to an entity (colony or spectrum)."""

  def __init__(self):
    judge_score.__init__(self)
    
    self.flag_human = True
  
  def make_judgement(self, score_code):
    """make_judgement() in this class means that a human has decided for a score code and this code is going to be passed to the classifier. 
    
    At this point the score code is validated."""
    
    if score_code <> None and score_code <> "None":
      try:
        self.score_codes.index(score_code)
  
        self.judgement = self.judgement_object()
        self.judgement.code = score_code
      except ValueError, e:
        raise error_x("Score code %s is invalid." % (score_code, ))
    else:
      self.judgement = self.judgement_object()
      self.judgement.code = None

      
    
