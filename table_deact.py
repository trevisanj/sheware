from table import *
from sql_mounter import *

class table_deact(table):
  table_name = "deact"

  def get_all_data(self, field_names=None):
    o = select_mounter(tables=(self.table_name,),
                       fields=field_names, orderbys="name")
    return con.execute(o.mount_select()).fetchall()

t_deact = table_deact()