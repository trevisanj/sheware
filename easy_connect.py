import sys
sys.path.append('setup')
import db_con
db_con.setup()
db_con.con.connect()
