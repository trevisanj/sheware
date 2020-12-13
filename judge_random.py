from judge_score import judge_score
import random

class judge_random(judge_score):
  """Represents a random judge. This may be useful either as an example or as statistical tool."""
  
  def make_judgement(self):
    self.judgement = self.judgement_object()
    self.judgement.code = self.score_codes[random.randint(0, self.score_count-1)]
    