from parameterized import parameterized

class judgement(parameterized):
  """Object meant to store judgements made by judge objects. Usually created and returned by jugde.judge() ."""

  def compare_to(self, other):
    """Compares itself to another judgement object. Must return True or False. Also sets self.cmp_output and self.cmp_result
    """
    
    self.cmp_result = self.get_default_value() == other.get_default_value()
    self.cmp_output = self.cmp_result and "Yes" or "No"
    
    return self.cmp_result
    
    