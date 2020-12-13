from table import table
from db_con import con
from sql_mounter import *
from errors import *

SEPARATOR = ":"
JOINER = SEPARATOR+" "


def score_str_to_list(s):
  """Parses string of lines. Each line must contain 'code: name'. Code will be uppercased.
  
  @return  ((code, name), (code, name) ...."""


  assert isinstance(s, (str, unicode))
  print "qweqwwe"
  
  i = 0
  scores = []
  for line in s.split("\n"):
    print "wwwwwwwwww"
    flag_ignore = False
    terms = line.split(SEPARATOR)
    if len(terms) <> 2:
      if len(terms) == 1 and len(terms[0]) == 0:
        flag_ignore = True
      else:
        raise error_x("line %s ('%s'): number of terms does not equal 2." % (i+1, line))
      
    if not flag_ignore:
      if min(map(lambda(s): len(s.strip()), terms)) == 0:
        raise error_x("line %s ('%s'): empty term." % (i+1, line))
  
      scores.append((terms[0].strip().upper(), terms[1].strip()))

  return scores

def score_list_to_str(l):
  """@return string 'code: name\\ncode: name\\n ...'"""
  
  
  s = "\n".join(map(lambda(score): JOINER.join(score), l))
  
  return s


def sanitize(s):
  """Sanitizes a score line string by dismounting and remounting it."""
  
  return score_list_to_str(score_str_to_list(s))




class table_score (table):
  def __init__(self):
    self.table_name = "score"

  def get_cursor_1scoregroup(self, field_names, idscoregroup):
    o = select_mounter(tables=self.table_name,
                       fields=field_names,
                       wheres="idscoregroup = %s" % idscoregroup,
                       orderbys="id")
    return con.execute(o.mount_select())
  
  def get_string_1scoregroup(self, idscoregroup):
    data = self.get_cursor_1scoregroup(("code", "name"), idscoregroup).fetchall()
    return "\n".join(map(lambda(row): ": ".join(row), data))


  def update_from_string(self, s, idscoregroup):
    # Checks all rows first
    i = 0
    
    lines = score_str_to_list(s)

    print "#####################################", lines

    con.execute("delete from %s where idscoregroup = %s" % (self.table_name, idscoregroup))
    
    for (code, name) in lines:
      self.insert({"code": code, "name": name, "idscoregroup": idscoregroup})



t_score = table_score()

if __name__ == "__main__":
  s = "A: Control untransformed\nB:Treated untransformed\nc: Control transformed\n\n\n\n    d     : Treated transformed\n"
  
  print "str before\n", s
  l = score_str_to_list(s)
  print "list after\n", l
  print "str after\n", score_list_to_str(l)
  