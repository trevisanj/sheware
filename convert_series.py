import easy_connect
import numpy

con = easy_connect.db_con.con

d_idsp = con.query_cursor("select id from spectrum").fetchall()

no_spectra = len(d_idsp)
i = 0
ii = 0

for (idspectrum,) in d_idsp:
  idexperiment = con.query_scalar("select idexperiment from series_ where idspectrum = %s limit 1" % idspectrum)
  
  if idexperiment == None:
    print "Ahaaaaaaaa: o spectrum sem dados eh o "
    print idspectrum
    
    con.query_cursor("update spectrum set flag_condemned = 1 where id = %s" % idspectrum)

  else:
	  d_curve = con.query_cursor("select value from series_ where idspectrum = %s order by id" % idspectrum).fetchall()
	  
	  s_curve = '['
	  i11 = 0
	  for n in numpy.array(d_curve):
	    if i11 > 0:
	      s_curve += ', '
	    s_curve += str(n[0])
	    i11 += 1
	  s_curve += ']'
	  
#	  s_curve = str(numpy.array(d_curve).transpose())
#	  s_curve = s_curve[1:len(s_curve)-1]

	  con.query_cursor("insert into series (idspectrum, idexperiment, iddomain, vector) values (%s, %s, 2, '%s')" % (idspectrum, idexperiment, s_curve))
  
  i += 1
  ii += 1
  
  if ii == 100:
    print "%f %% ..." % (100.*i/no_spectra)
    ii = 0
