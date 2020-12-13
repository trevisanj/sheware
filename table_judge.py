from table import table
from db_con import con
from output import output
from sql_mounter import select_mounter
from errors import *


class table_judge(table):
  def __init__(self):
    self.table_name = "judge"
    
  def assure_can_delete(self, id_):
     if (con.query_scalar("select count(*) from colony_judge where idjudge = %s" % id_) > 0) or \
        (con.query_scalar("select count(*) from spectrum_judge where idjudge = %s" % id_) > 0):
       raise error_x("Classifier cannot be deleted because it is being used!")
     
    
  def get_cursor_joined_scoregroup(self, field_names):
    o = select_mounter(tables="judge",
                       fields=field_names,
                       joins=(("scoregroup", "scoregroup.id = judge.idscoregroup"),),
                       orderbys="judge.name")
    return con.execute(o.mount_select())                       

    
t_judge = table_judge()