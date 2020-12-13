from db_con import con
con.user_name = "root"
con.db_name = "cells"
con.connect()


class t(object):
  def go(self):
    exec """
import judge_human
cl = judge_human.judge_human(1)
"""
    
    print cl
    
    return cl

o = t()
cl = o.go()
print cl