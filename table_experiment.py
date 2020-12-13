from table import table
from table_tray import t_tray
from sql_mounter import *
from db_con import con
class table_experiment (table):
  def __init__(self):
    self.table_name = "experiment"

  def delete(self, id_):
    """This method cascade-deletes db:tray records."""
    
    self.assure_can_delete(id_)
    
    t_tray.delete_1experiment(id_)
    con.execute("delete from %s where id = %s" % (self.table_name, id_))
    con.execute("delete from %s where id = %s" % (self.table_name, id_))


  def get_cursor_with_spectrum_count(self, field_names):
    """returns the a con.db_result object of 'select <fields[0]>, ... from <table_name>' or * fields if fields == None
    """
    
    o = select_mounter(tables="experiment",
                       fields=field_names,
                       joins=(("tray", "tray.idexperiment = experiment.id"),
                              ("slide", "slide.idtray = tray.id"),
                              ("colony", "colony.idslide = slide.id"),
                              ("spectrum", "spectrum.idcolony = colony.id")),
                       groupbys="experiment.id",
                       orderbys="experiment.id")
    return con.execute(o.mount_select())
  
    
t_experiment = table_experiment()