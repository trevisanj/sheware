from table_judge import t_judge
from table_score import t_score
from judge import judge
from judgement_score import judgement_score

class judge_score(judge):
  """Judges which use the scores table.
  
  It maintains a score list."""

  __score_count = 0
  
  def set_idjudge(self, idjudge):
    """Overrides the judge original method because it is necessary to retrieve the scores list."""
    self.__idjudge = idjudge
    
    if idjudge <> None:
      (idscoregroup, params) = t_judge.get_values_from_id(("idscoregroup", "params"), idjudge)
      self.set_idscoregroup(idscoregroup)
      self.set_params(params)
        

  def set_idscoregroup(self, value):
    self.__idscoregroup = value
    
    self.idscore_s = []
    self.score_codes = []
    self.__score_count = 0
 
    if value <> None:
      data = t_score.get_cursor_1scoregroup(("id", "code"), value).fetchall()
      self.__score_count = len(data)

      # Populates score ids and codes.
      for (id, code) in data:
        self.idscore_s.append(id)
        self.score_codes.append(code)


  idjudge = property(lambda(self): self.__idjudge, set_idjudge)
  idscoregroup = property(lambda(self): self.__idscoregroup, set_idscoregroup)
  score_count = property(lambda(self): self.__score_count) 

  def get_explanation1(self):
    """Returns a string explaining the possible score codes."""
    return t_score.get_string_1scoregroup(self.idscoregroup)


  def judgement_object(self):
    return judgement_score()