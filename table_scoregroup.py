from table import table
from db_con import con
from table_score import t_score

class table_scoregroup (table):
  def __init__(self):
    self.table_name = "scoregroup"
    
  def update(self, values, id_):
    """Sanitizes scores string (with possible exception raising) before updating the database (i.e. calling table.update())."""
    
    flag_scores = False
    try:
      scores = values["scores"]
      flag_scores = True
    except:
      pass
    if flag_scores:
      #values["scores"] = sanitize(values["scores"])
      t_score.update_from_string(values["scores"], id_)
      del(values["scores"])
    
    table.update(self, values, id_)

  def insert(self, values):
    flag_scores = False
    try:
      scores = values["scores"]
      del(values["scores"])
      flag_scores = True
    except:
      pass

    table.insert(self, values)
    id_ = con.insert_id()



    if flag_scores:
      #values["scores"] = sanitize(values["scores"])
      t_score.update_from_string(scores, id_)

    


  def delete(self, id_):
    self.assure_can_delete(id_)
    
    con.execute("delete from score where idscoregroup = %s" % id_)
    con.execute("delete from %s where id = %s" % (self.table_name, id_))
    
  
      
t_scoregroup = table_scoregroup()

