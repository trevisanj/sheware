from judgement import judgement
from param_def import *

class judgement_float(judgement):
  """This judgement class is meant to be used for judges which calculate a float number based on a spectrum. The only param is called 'value'."""
  def init_param_defs(self):
    self.param_defs = (param_def(name="value"),)
