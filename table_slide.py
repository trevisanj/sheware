from table import table
from db_con import con
from output import output
from sql_mounter import select_mounter
from table_colony import t_colony

class table_slide (table):
  def __init__(self):
    self.table_name = "slide"

  def delete_1tray(self, idtray):
    data = self.get_cursor_1tray(("id",), idtray).fetchall()
    if len(data) > 0:
      i = 0
      for id_ in apply(zip, data)[0]:
        self.delete(id_)
        i += 1
        
      output("--------- deleted "+str(i)+" slides from idtray= "+str(idtray))

  
  def delete(self, id_):
    """This method cascade-deletes cells.slide records."""
    
    self.assure_can_delete(id_)
    
    t_colony.delete_1slide(id_)
    con.execute("delete from %s where id = %s" % (self.table_name, id_))


  def assure(self, code, idtray, flag_simulation = False):
    flag_inserted = False
    id_ = con.query_scalar("select id from %s where code = %%s and idtray = %%s" % self.table_name, (code, idtray))
    if id_ == None:
      if not flag_simulation:
        con.execute("insert into %s (code, idtray) values(%%s, %%s)" % self.table_name, (code, idtray))
        id_ = con.insert_id()
      else:
        id_ = 0
      output("+++ +++ Slide inserted: (%s, '%s')" % (id_, code))
      flag_inserted = True
    return (flag_inserted, id_)

  def get_cursor_1tray(self, field_names, idtray):
    o = select_mounter(tables=self.table_name,
                       fields=field_names,
                      wheres="idtray = %s" % idtray,
                      orderbys="code")
    return con.execute(o.mount_select())

  def import_picture(self, file_name, id_):
    from image_opener import image_opener
    con.execute("update %s set picture = %%s where id = %s" % (self.table_name, id_), image_opener(file_name=file_name, max_pixels=2e5).to_string())

   
  def get_cursor_1tray_with_spectrum_count(self, field_names, idtray):
    o = select_mounter(tables="slide",
                       fields=field_names,
                       joins=(("colony", "colony.idslide = slide.id"),
                              ("spectrum", "spectrum.idcolony = colony.id")),
                       groupbys="slide.id",
                       wheres="idtray = %s" % idtray,
                       orderbys="slide.code")
    return con.execute(o.mount_select())
  
   
t_slide = table_slide()