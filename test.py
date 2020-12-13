from db_con import con
con.user_name = "root"
con.db_name = "cells"
con.connect()


class t(object):
  def go(self):
    s = """
import judge_human
    """
    
    o = compile(s, "here", "single")
    eval(o)
    
    
    s = """
cl = judge_human.judge_human(1)
    """
    
    o = compile(s, "here", "single")
    eval(o)
    
#    print cl
    
#    return cl

o = t()
o.go()
print cl