class param_def(object):
  """Single parameter definition."""
  def __init__(self, name = None, type = None, flag_required = None):
    self.name = name
    self.type = type
    self.flag_required = False    
