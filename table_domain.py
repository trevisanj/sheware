from table import table
from db_con import con
from output import output
from sql_mounter import select_mounter
from errors import *


class table_domain(table):
  def __init__(self):
    self.table_name = "domain"
    
  def assure_can_delete(self, id_):
     if (con.query_scalar("select count(*) from series where iddomain = %s" % id_) > 0) or \
        1:
       raise error_x("Domain cannot be deleted because it is being used!")


#   def get_cursor(self, field_names, idexperiment):
#     o = select_mounter(tables=("domain"),
#                        fields=field_names,
#                        orderbys="domain.name")
#                        
# #    flag_active_only = 1
# #    if flag_active_only:
# #      o.add_where("flag_active = 1")
# 
#     return con.execute(o.mount_select())                       



t_domain = table_domain()