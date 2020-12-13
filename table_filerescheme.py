from table import table
from db_con import con
from output import output
from sql_mounter import select_mounter
from table_colony import t_colony

class table_filerescheme (table):
  def __init__(self):
    self.table_name = "filerescheme"
  
   
t_filerescheme = table_filerescheme()