from judge import judge
from errors import *
from judgement_grade import judgement_grade

class judge_grade_human(judge):
  """Test human judge who is supposed to assign an entity a grade from 0 to 10."""

  def __init__(self):
    judge.__init__(self)
    self.flag_human = True
    
  def get_explanation1(self):
    return "0..10"
    
  def judgement_object(self):
    return judgement_grade()
    
  def make_judgement(self, grade):
    
    if grade <> None and grade <> "None":
      grade = int(grade)
      if not grade in range(0, 11):
        raise error_x("Grade '%s' is invalid." % (grade, ))
  
      self.judgement = self.judgement_object()
      self.judgement.grade = grade
    else:
      self.judgement = judgement_grade()
      self.judgement.grade = None

      
    
