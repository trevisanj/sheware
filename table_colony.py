from table import table
from db_con import con
from output import output
from sql_mounter import select_mounter
from table_spectrum import t_spectrum
from table_colony_judge import t_colony_judge

class table_colony (table):
  def __init__(self):
    self.table_name = "colony"



  def assure(self, code, idslide, flag_simulation = False):
    flag_inserted = False
    id_ = con.query_scalar("select id from %s where code = %%s and idslide = %%s" % self.table_name, (code, idslide))
    if id_ == None:
      print "ttttttttttttttttttttttttttttttttttttttttttttttray da new colony e de brinde o slide id e code"
      print con.execute("select tray.id, tray.code, slide.id, slide.code from slide left join tray on tray.id = slide.idtray where slide.id = "+str(idslide)).fetchall()
      print "mas o COLONY CODE EH "+str(code)
      if not flag_simulation:
        con.execute("insert into %s (code, idslide) values(%%s, %%s)" % self.table_name, (code, idslide))
        id_ = con.insert_id()
      else:
        id_ = 0
      output("+++ Colony inserted: (%s, '%s')" % (id_, code))
      flag_inserted = True
    return (flag_inserted, id_)

    
#  def reset(self, code, idslide):
#    """Verifies colony code existence. exists: deletes all child series; does not exist: inserts colony row.
#    """
#    
#    id_ = con.query_scalar("select id from %s where code = %%s and idslide = %%s" % self.table_name, (code, idslide))
#    if id_ == None:
#      con.execute("insert into %s (code, idslide) values(%%s, %%s)" % self.table_name, (code, idslide))
#      id_ = con.insert_id()
#      output("Sample inserted: (%s, '%s')" % (id_, code))
#    else:
#      t_spectrum.delete_1colony(id_)
#    return id_
  
  
  def delete_1slide(self, idslide):
    data = con.execute(select_mounter(tables="colony",
                                      fields=("id",),
                                      wheres="idslide = %s" % idslide,
                                      orderbys="code").mount_select()).fetchall()

    if len(data) > 0:
      i = 0
      for id_ in apply(zip, data)[0]:
        self.delete(id_)
        i += 1
        
      output("------ deleted "+str(i)+" colonies from idslide= "+str(idslide))

    
  
  def delete(self, id_):
    """This method cascade-deletes db:colony records."""
    
    self.assure_can_delete(id_)
    
    t_spectrum.delete_1colony(id_)
    t_colony_judge.delete_1colony(id_)
    con.execute("delete from %s where id = %s" % (self.table_name, id_))
  
  

  
  def get_cursor_joined(self, idexperiment):
    o = select_mounter(tables="colony",
                       fields=("tray.code as tray_code", "slide.code as slide_code", "colony.id as colony_id", "colony.code as colony_code"),
                       joins=(("slide", "slide.id = colony.idslide"), ("tray", "tray.id = slide.idtray")),
                       wheres="tray.idexperiment = %s" % idexperiment,
                       orderbys="colony.code")
    return con.execute(o.mount_select())                       

  def get_cursor_joined_params(self, idexperiment, idjudge):
    o = select_mounter(tables=("spectrum", "colony"),
                       fields=("tray.code as tray_code", "slide.code as slide_code", "colony.id as colony_id", "count(spectrum.id) as no_spectrums", "colony.code as colony_code", "colony_judge.params"),
                       joins=(("slide", "slide.id = colony.idslide"), 
                              ("tray", "tray.id = slide.idtray"), 
                              ("colony_judge", "colony_judge.idcolony = colony.id AND colony_judge.idjudge = %s" % (idjudge,))
                             ),
                       wheres=("tray.idexperiment = %s" % (idexperiment,), "spectrum.idcolony = colony.id"),
                       groupbys="colony.id",
                       orderbys="colony.code")
    return con.execute(o.mount_select())                       
                           

  def get_cursor_1slide(self, field_names, idslide):
    o = select_mounter(tables="colony",
                       fields=field_names,
                       wheres="idslide = %s" % idslide,
                       orderbys="colony.code")
    return con.execute(o.mount_select())

    
  def get_cursor_1slide_with_spectrum_count(self, field_names, idslide):
    o = select_mounter(tables="colony",
                       fields=field_names,
                       joins=(("spectrum", "spectrum.idcolony = colony.id"),),
                       groupbys="colony.id",
                       wheres="idslide = %s" % idslide,
                       orderbys="colony.code")
    return con.execute(o.mount_select())


t_colony = table_colony()