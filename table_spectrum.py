from table import table
from db_con import con
from table_series import t_series
from sql_mounter import *
from table_spectrum_judge import t_spectrum_judge
from table_colony_judge import t_colony_judge
from output import *

class table_spectrum (table):
  def __init__(self):
    self.table_name = "spectrum"
  
#  def get_cursor_1colony(self, field_names, idcolony, flag_active_only=False):
#    o = select_mounter(tables=self.table_name,
#                       fields=field_names,
#                       wheres="idcolony = %s" % idcolony,
#                       orderbys="id")
#    if flag_active_only:
#      o.add_where("flag_inactive is null or flag_inactive = 0")
#    return con.execute(o.mount_select())
  
  
  def delete_1colony(self, idcolony):
    data = self.get_cursor_data(("id",), idcolony=idcolony).fetchall()
    if len(data) > 0:
      i = 0
      for id_ in apply(zip, data)[0]:
        self.delete(id_)
        i += 1
      
      output("--- deleted "+str(i)+" spectra from idcolony = "+str(idcolony))
        
    
  
  def delete(self, id_):
    """This method cascade-deletes db:series records."""
    
    self.assure_can_delete(id_)
    
    t_series.delete_1spectrum(id_)
    t_spectrum_judge.delete_1spectrum(id_)
    con.execute("delete from %s where id = %s" % (self.table_name, id_))

  def get_cursor_ids_1experiment(self, idexperiment, flag_active_only=False):
    return self.get_cursor_1experiment(("spectrum.id",), idexperiment, flag_active_only)
    

  def get_cursor_1experiment(self, field_names, idexperiment, flag_active_only=False, orderbys=None):
    if orderbys == None:
      ("colony.code", "spectrum.file_name")
    o = select_mounter(tables=("spectrum",),
                       fields=field_names,
                       joins=(("colony", "colony.id = spectrum.idcolony"), 
                              ("slide", "slide.id = colony.idslide"), 
                              ("tray", "tray.id = slide.idtray")
                             ),
                       wheres=("tray.idexperiment = %s" % (idexperiment,)),
                       orderbys=orderbys)
    if flag_active_only:
      o.add_where("flag_active = 1")
    return con.execute(o.mount_select())                       



#  def get_cursor_joined_params(self, idexperiment, idjudge, flag_active_only=False):
#    """This function is obsolete, please use get_cursor_data() if possible"""
#    o = select_mounter(tables=("spectrum"),
#                       fields=("spectrum.id", "spectrum_judge.params"),
#                       joins=(("colony", "colony.id = spectrum.idcolony"), 
#                              ("slide", "slide.id = colony.idslide"), 
#                              ("tray", "tray.id = slide.idtray"), 
#                              ("spectrum_judge", "spectrum_judge.idspectrum = spectrum.id AND spectrum_judge.idjudge = %s" % (idjudge,))
#                             ),
#                       wheres=("spectrum.idexperiment = %s" % (idexperiment,),),
#                       orderbys=("spectrum.idcolony", "spectrum.id"))
#    if flag_active_only:
#      o.add_where("flag_active = 1")
#    return con.execute(o.mount_select())                       


  def reset(self, file_name, idexperiment, iddomain, idcolony, flag_simulation = False):
    """Verifies if file_name already exists in the colony identified by idcolony.
         exists: deletes all child series; 
         does not exist: inserts spectrum row.
    """
    
    flag_inserted = False
    id_ = con.query_scalar("select id from %s where file_name = %%s and idcolony = %%s" % self.table_name, (file_name, idcolony))
    if id_ == None:
      if not flag_simulation:
        con.execute("insert into %s (file_name, idcolony, idexperiment) values(%%s, %%s, %%s)" % self.table_name, (file_name, idcolony, idexperiment))
        id_ = con.insert_id()
      else:
        id_ = 0
      output("+ Spectrum inserted: (%s, '%s')" % (id_, file_name))
      flag_inserted = True
    return (flag_inserted, id_)
  

  
  def insert(self, values):
    """Calls table.insert() and then insert rows into db:spectrum_judge as a cascade effect of rows contained in db:colony_judge.
    
    It means the new spectrum will have assigned all judge information assigned to its colony.
    """
    
    table.insert(self, values)
    id_ = con.insert_id()
    
    
    data = t_colony_judge.get_cursor_1colony(("idjudge", "params", "idexperiment"), values["idcolony"]).fetchall()
    
    for (idjudge, params, idexperiment) in data:
      t_spectrum_judge.insert({"idspectrum": id_, "idjudge": idjudge, "params": params, "idexperiment": idexperiment})
    

  def get_cursor_data(self, field_names=None, iddomain=None, iddeact = None, 
     idspectrum=None, idcolony=None, idslide=None, idtray=None, idexperiment=None, 
     idjudge_s = (), flag_active_only=False, 
     flag_join_colony=False, flag_join_slide=False, flag_join_tray=False, flag_join_experiment=False, 
     wheres=None, joins=None, groupbys=None, orderbys=None):
    """Returns a mysql cursor.
    
    If iddeact is passed, the SELECT will have a JOIN to cells.deact_spectrum.
      If flag_active_only is False then a "flag_active" field will be added to field_names  
    
    If idjudge_s is passed, :
      - the SELECT will have JOIN's to cells.spectrum_judge.
      - (param1, param2, ...) are added to field_names, corresponding to values in idjudge_s

    >idcolony< and idexperiment are exclusive

    field_names could be ("spectrum.id", "spectrum.idcolony", "series.vector")
    """
    
    groupbys = groupbys <> None and list(groupbys) or [];
    wheres = wheres <> None and list(wheres) or [];
    fields = field_names <> None and list(field_names) or [];
    joins = joins <> None and list(joins) or [];
    orderbys = orderbys <> None and list(orderbys) or ["spectrum.idcolony", "spectrum.id"];
    

    # Useful cascade joins: colony->slide->tray->experiment    
    if flag_join_experiment or flag_join_tray or flag_join_slide or flag_join_colony:
      joins.append(("colony", "colony.id = spectrum.idcolony"))
    if flag_join_experiment or flag_join_tray or flag_join_slide:
      joins.append(("slide", "slide.id = colony.idslide"))
    if flag_join_experiment or flag_join_tray:
      joins.append(("tray", "tray.id = slide.idtray"))
    if flag_join_experiment:
      joins.append(("experiment", "experiment.id = spectrum.idexperiment")) # alternative: tray.idexperiment (?)
    
    # Handles id spectrum or idcolony or idslide or idtray or idexperiment
    if idspectrum:
      wheres.append("spectrum.id = %d" % idspectrum)
    elif idcolony:
      wheres.append("spectrum.idcolony = %d" % idcolony)    
    elif idslide:
      wheres.append("colony.idslide = %d" % idslide)    
    elif idtray:
      wheres.append("slide.idtray = %d" % idtray)    
    elif idexperiment:
      wheres.append("spectrum.idexperiment = %d" % idexperiment)
    
    # Handles domain
    if iddomain:
      joins.append(("series", "series.idspectrum = spectrum.id and series.iddomain = %d" %iddomain))

    # Handles activation scheme    
    if iddeact:
      joins.append(("deact_spectrum", " deact_spectrum.idspectrum = spectrum.id and deact_spectrum.iddeact = %d" % iddeact))
      
      if flag_active_only:
        wheres.append("flag_inactive is null or flag_inactive = 0")


      else:
        pass
      # flag_active is easily retrieved by:
      #    sum(flag_inactive is not null and flag_inactive = 1) as flag_inactive
      #    sum(flag_inactive is null or flag_inactive = 0) as flag_active
    
    # Handles judges
    i = 1
    for idjudge in idjudge_s:
      joins.append(("spectrum_judge as sj%d" % i, "sj%d.idspectrum = spectrum.id and sj%d.idjudge = %d" % (i, i, idjudge)))
      fields.append("sj%d.params as params%d" % (i, i))
      i += 1
    
    print 'queria ver........................................'
    print fields
    print joins
    print wheres
    
    o = select_mounter(tables=("spectrum"),
                       fields=fields,
                       joins=joins,
                       wheres=wheres,
                       orderbys=orderbys,
                       groupbys=groupbys)

    print 'ENTAO OLHA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
    print o.mount_select()

    return con.execute(o.mount_select())                       




t_spectrum = table_spectrum()