from table import table
from db_con import con
from output import *
from sql_mounter import select_mounter
from table_judge import t_judge
from table_score import t_score
from table_spectrum_judge import t_spectrum_judge
from errors import *

class table_colony_judge (table):
  def __init__(self):
    self.table_name = "colony_judge"


  def delete_1colony(self, idcolony):
    con.execute("delete from %s where idcolony = %s" % (self.table_name, idcolony))
    
    
  def scores_to_idscore_s(self, scores, idjudge):
    """Resolves literal scores and returns a list of integer db:score.id values."""
    idscoregroup = t_judge.get_value_from_id("idscoregroup", idjudge)
    data_score = t_score.get_cursor_1scoregroup(("id", "code"), idscoregroup).fetchall()
    (score_ids, score_codes) = apply(zip, data_score)
    
    score_codes = list(score_codes)
    
    print score_ids, score_codes, type(score_codes[0]), type(scores[0])
    print scores[0], score_codes[0], str(scores[0]) == score_codes[0]
    
    i = 0    

    result = []
    for score in scores:
      if score <> None and score <> "None":
        try:
          index = score_codes.index(score.upper())
        except:
          raise error_x("Line %s: invalid score: '%s'" % (i+1, score))
        result.append(score_ids[index])
      else:
        result.append(-1)

      i += 1

    return result
    

  def update(self, idcolony_s, params_s, idjudge, idexperiment):
    """Two-stage
    
    1. sql:delete-insert sequence first vanishing all cells.colony_judge data related to @idjudge and then re-inserting one record for
    each (@idcolony_s[i], @params_s[i]) for all i in the range.
    
    2. Cascade-deletes-inserts records in cells.spectrum_judge."""
    
    con.execute("delete from %s where idjudge = %s and idexperiment = %s" % (self.table_name, idjudge, idexperiment))
    t_spectrum_judge.delete_1judge(idjudge, idexperiment)
    
    no = len(idcolony_s)
    ii = 0
    
    for i in range(0, len(idcolony_s)):
      con.execute("insert into %s (idcolony, idjudge, params, idexperiment) values (%%s, %%s, %%s, %%s)" % self.table_name, 
          (idcolony_s[i], idjudge, params_s[i], idexperiment))
          
      t_spectrum_judge.insert_1colony(params=params_s[i], idjudge=idjudge, idcolony=idcolony_s[i], idexperiment=idexperiment)
      
      ii += 1
      if ii == 45:
        progress(float(i+1)/no)
        ii = 0
        
    progress(1)

    
#  def update(self, idcolony_s, scores, idjudge):
#    
#    idscore_s = self.scores_to_idscore_s(scores, idjudge)
#      
#   con.execute("delete from %s where idjudge = %s" % (self.table_name, idjudge))
#    t_spectrum_judge.delete_1judge(idjudge)
#    
#    for i in range(0, len(idcolony_s)):
#      if idscore_s[i] > 0:
#        con.execute("insert into %s (idcolony, idjudge, idscore) values (%%s, %%s, %%s)" % self.table_name, 
#            (idcolony_s[i], idjudge, idscore_s[i]))
#          
#        t_spectrum_judge.insert_1colony(idscore=idscore_s[i], idjudge=idjudge, idcolony=idcolony_s[i])
        
    
    
    
t_colony_judge = table_colony_judge()