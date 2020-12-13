"""SQL statement mounters."""

class select_mounter(object):
  sql = ""
  
  def __init__(self, tables=None, fields=None, wheres=None, joins=None, orderbys=None, groupbys=None):
    self.tables = []
    self.fields = []
    self.wheres = []
    self.joins = []
    self.orderbys = []
    self.groupbys = []

    if tables <> None:
      self.add_table(tables)
    if fields <> None:
      self.add_field(fields)
    if wheres <> None:
      self.add_where(wheres)
    if joins <> None:
      self.add_join(joins)
    if orderbys <> None:
      self.add_orderby(orderbys)
    if groupbys <> None:
      self.add_groupby(groupbys)
      
  def add_something(self, what, x):
    """ what must be a valid variable name"""
    
    if isinstance(x, (list, tuple, dict)):
      for xx in x:
        assert isinstance(xx, str)
        
      self.__setattr__(what, self.__getattribute__(what)+list(x))
    else:
      assert isinstance(x, str)
      self.__setattr__(what, self.__getattribute__(what)+[x])
        
  def add_table(self, x):
    self.add_something("tables", x)

  def add_field(self, x):
    self.add_something("fields", x)

  def add_where(self, x):
    self.add_something("wheres", x)

  def add_join(self, x):
    what = "joins"
    if isinstance(x, (list, tuple, dict)):
      for xx in x:
        assert isinstance(xx, tuple)
        assert len(xx) == 2
        
      self.__setattr__(what, self.__getattribute__(what)+list(x))
    else:
      assert isinstance(x, tuple)
      assert len(x) == 2
      self.__setattr__(what, self.__getattribute__(what)+[x])

  def add_orderby(self, x):
    self.add_something("orderbys", x)

  def add_groupby(self, x):
    self.add_something("groupbys", x)
  
  def mount_select(self):
    s = "SELECT "+(", ".join(self.fields))+" FROM "+(", ".join(self.tables))
    
    if len(self.joins) > 0:
      for a in self.joins:
        s += " LEFT JOIN "+a[0]+" ON "+a[1]
        
    if len(self.wheres) > 0:
      s += " WHERE "+(" AND ".join(self.wheres))
      
    if len(self.groupbys) > 0:
      s += " GROUP BY "+(", ".join(self.groupbys))
      
    if len(self.orderbys) > 0:
      s += " ORDER BY "+(", ".join(self.orderbys))
      
    self.sql = s
    
    return s
  