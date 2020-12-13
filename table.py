from db_con import *
from errors import *
from sql_mounter import *

class table(object):
  table_name = ""

  def assure_can_delete(self, id_):
    """This method must raise an exception if the row cannot be deleted."""
    pass
  
  def delete(self, id_):
    self.assure_can_delete(id_)
    con.execute("delete from %s where id = %s" % (self.table_name, id_))
 
  
  def get_name_from_id(self, id_):
    return self.get_value_from_id("name", id_)
  
  def get_value_from_id(self, field_name, id_):
    cursor = con.execute("select %s from %s where id = %s" % (field_name, self.table_name, id_))
    t = cursor.fetchone()
    cursor.close()
    if t == None:
      raise error_x("Id '%s' does not exist in table '%s'." % (id_, self.table_name))
    return t[0]
  
  def get_values_from_id(self, fields, id_):
    cursor = con.execute("select %s from %s where id = %s" % (",".join(fields), self.table_name, id_))
    t = cursor.fetchone()
    cursor.close()
    return t


  def get_cursor(self, field_names=None, joins=None, wheres=None, groupbys=None, orderbys=None):
    """returns the a con.db_result object of 'select <fields[0]>, ... from <table_name>' or * fields if fields == None
    """
    
    if field_names == None:
      field_names = ["*"]

#    sql = "select %s from %s" % (s_fields, self.table_name)
#    return con.query_cursor(sql)

    o = select_mounter(tables=(self.table_name,),
                       fields=field_names,
                       orderbys=orderbys,
                       joins=joins,
                       wheres=wheres,
                       groupbys=groupbys)
    return con.execute(o.mount_select())

  
  def get_all_data(self, field_names=None):
    o = select_mounter(tables=(self.table_name,),
                       fields=field_names) #, orderbys="name")
    return con.execute(o.mount_select()).fetchall()
    
  
  def insert(self, values):
    con.execute(("insert into %s (" % (self.table_name,))+",".join(values.keys())+
                ") values ("+("%s"+", %s"*(len(values)-1))+")", 
                tuple(values.values()))
    

  def update(self, values, id_):
    assert isinstance(values, dict)
    
    print "--------------- table.py update()"
    print ("update %s set "+(" = %%s, ".join(values.keys()))+" = %%s where id = %s") % (self.table_name, id_), tuple(values.values())
    con.execute(("update %s set "+(" = %%s, ".join(values.keys()))+" = %%s where id = %s") % (self.table_name, id_), tuple(values.values()))
    
    
