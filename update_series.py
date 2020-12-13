from sql_mounter import *
import easy_connect
from table_series import *
from db_con import con

o = select_mounter(tables=("spectrum",),
                   fields=("tray.idexperiment", "spectrum.id"),
                   joins=(("colony", "colony.id = spectrum.idcolony"), 
                          ("slide", "slide.id = colony.idslide"), 
                          ("tray", "tray.id = slide.idtray")
                         ))
data = con.execute(o.mount_select()).fetchall()
no = len(data)
i = 0
ii = 0
for (idexperiment, idspectrum) in data:
  con.execute("update series set idexperiment = %s where idspectrum = %s" % (idexperiment, idspectrum))
  i += 1
  ii += 1
  if ii == 100:
    print "%5.1f %%" % (float(i+1)/no*100)
    ii = 0
    
print("Done.")

                   