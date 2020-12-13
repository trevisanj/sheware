"""This module is intended to provide shortcuts to some information in the database."""

from db_con import con
from output import *

def get_row_count(table_name):
  return con.query_scalar("select count(*) from %s" % table_name)
    
def get_table_names():
  a = con.query_table("show tables")
  l = []
  for aa in a:
    l.append(aa[0])
  return l



def show_summary():
    
  tables = get_table_names()
  max_len = max(map(len, tables))

  output("Row count for database tables")
  for table_name in tables:
    output(table_name.ljust(max_len)+(" %5d" % get_row_count(table_name)))
