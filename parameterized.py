class parameterized(object):
  """Objects that accept parameters in form of a parameter string"""

  
  
  def __init__(self):
    self.param_defs = ()
    self.init_param_defs()
    self.init_params()
  
  
  def init_param_defs(self):
    """This method must be inherited. It is called automatically in __init__(). Its task is to define self.param_defs as a list (or tuple) of param_def objects"""
    pass
  
  def init_params(self):
    """Creates attributes listed in param_defs and sets their default value (currently None)"""
    
    for param_def in self.param_defs:
      self.__setattr__(param_def.name, None)
  
  def get_params(self):
    """Converts internal parameters to a parameter string to be stored in db:judge.params. Abstract method."""
        
    def vlw(name):
      o = self.__getattribute__(name)
      if isinstance(o, (str, unicode)):
        return "\""+o+"\""
      else:
        return str(o)
      
    return "".join([pdef.name+" = "+vlw(pdef.name)+"\n" for pdef in self.param_defs])
  
  def set_params(self, params):
    """Parses parameter string and assigns internal parameters."""
    
   
    if isinstance(params, str):
      #print "olha aih ===>", params
      for line in params.split("\n"):
        if len(line) > 0:
          # this technique allows '=' characters to be inside values
          pos = line.index("=")
          name = line[0:pos].strip().lower()
          value = line[pos+1:].strip()
        
          self.__setattr__(name, eval(value))

  def get_default_value(self):
    return self.__getattribute__(self.param_defs[0].name)
