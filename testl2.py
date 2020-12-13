class list2(list):
  def __init__(self, table):
    self.table = table
    list.__init__(self)
    
  def show1st(self):
    print "olhaih:", self[0]