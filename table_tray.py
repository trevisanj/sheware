from table import table
from db_con import con
from output import output
from sql_mounter import select_mounter
from errors import *
from table_slide import t_slide

class table_tray (table):
  def __init__(self):
    self.table_name = "tray"

  def delete(self, id_):
    """This method cascade-deletes db:slide records."""
    
    self.assure_can_delete(id_)
    
    t_slide.delete_1tray(id_)
    con.execute("delete from %s where id = %s" % (self.table_name, id_))
    output("------------ Tray "+str(id_)+" deleted")


  def assure(self, code, _idexperiment, flag_simulation = False):
    flag_inserted = False
    row = con.query_row("select id from %s where code = %%s and idexperiment = %%s" % self.table_name, (code, _idexperiment))
    if row == None:
      if not flag_simulation:
        con.execute("insert into %s (code, idexperiment) values(%%s, %%s)" % self.table_name, (code, _idexperiment))
        id_ = con.insert_id()
      else:
        id_ = 0
      output("+++ +++ +++ Tray inserted: (%d, '%s')" % (id_, code))
      flag_inserted = True
    else:
      id_ = row[0]
      
    return (flag_inserted, id_)
   
  def get_cursor_1experiment(self, field_names, idexperiment):
    o = select_mounter(tables=self.table_name,
                       fields=field_names,
                      wheres="idexperiment = %s" % idexperiment,
                      orderbys="code")
    return con.execute(o.mount_select())
  
  def import_picture(self, file_name, id_):
    from image_opener import image_opener
    con.execute("update %s set picture = %%s where id = %s" % (self.table_name, id_), image_opener(file_name=file_name, max_pixels=1e6).to_string())
    
  def delete_1experiment(self, idexperiment):
    data = self.get_cursor_1experiment(("id",), idexperiment).fetchall()
    if len(data) > 0:
      for id_ in apply(zip, data)[0]:
        self.delete(id_)

  def get_cursor_1experiment_with_spectrum_count(self, field_names, idexperiment):
    o = select_mounter(tables="tray",
                       fields=field_names,
                       joins=(("slide", "slide.idtray = tray.id"),
                              ("colony", "colony.idslide = slide.id"),
                              ("spectrum", "spectrum.idcolony = colony.id")),
                       groupbys="tray.id",
                       wheres="tray.idexperiment = %s" % idexperiment,
                       orderbys="tray.code")
    return con.execute(o.mount_select())
  
    
t_tray = table_tray()