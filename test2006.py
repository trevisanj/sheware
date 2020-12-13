from easy_connect import *

input('COnnected, now show the fucking server down')

try:
	print db_con.con.query_cursor("select id, name from experiment").fetchall()
except Exception, e:
  print e.message
