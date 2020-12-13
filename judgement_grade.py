from judgement import judgement
from param_def import *

class judgement_grade(judgement):
  def init_param_defs(self):
    self.param_defs = (param_def(name="grade"),)
