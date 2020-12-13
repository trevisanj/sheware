class error_x(Exception):
  flag_silent = False # If True, a MessageBox is not to be shown in the presence of this error.
  
  def __init__(self, s, caller = None):
    if caller:
      s = "["+caller.__clas__+"] "+s
    Exception.__init__(self, s)
    
class error_abort(error_x):
  flag_silent = True