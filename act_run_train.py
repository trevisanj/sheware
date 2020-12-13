from session import session
from output import *
from table_judge import t_judge
from table_spectrum import t_spectrum
from table_series import t_series
from table_spectrum_judge import t_spectrum_judge
from errors import *
from judge import *
from spectrum_lot import spectrum_lot


def run(idjudge):
  if idjudge == -1000: # all
    wheres=["judge.class_name not like '%human%'"]
  else:
    wheres=["judge.id = "+str(idjudge)]
  data = t_judge.get_cursor(field_names=["id", "class_name"], wheres=wheres).fetchall()
  idjudge_s = map(lambda row: row[0], data)
  class_names = map(lambda row: row[1], data)
  
  # makes the judge objects
  
  jg_s = []
  for i in range(0, len(class_names)):
    jg = judge_object(class_names[i])
    if jg.flag_human:
      raise error_x("This is a human judge. Cannot run a human judge.")
    
    jg_s.append(jg)
    jg_s[i].idjudge = idjudge_s[i]

  
  # spectrum_lot object contains the actual spetrum curves
  lot = spectrum_lot()
  lot.flag_active_only = False
  lot.idexperiment = session.idexperiment
  lot.iddomain = session.iddomain
  lot.iddeact = session.iddeact
  lot.read()

  for i in range(0, len(jg_s)):
    jg_s[i].lot = lot
  
  # cleans all judgement records
  for i_jg in range(0, len(idjudge_s)):
    output("^^^ Processing "+str(idjudge_s[i_jg])+" "+class_names[i_jg])
  
    try:
      output("Deleting prior judgements...")  
      t_spectrum_judge.delete_1judge(idjudge_s[i_jg], session.idexperiment)
    
      # list of all spectrum ids
      #
      idspectrum_s = lot.get_idspectrum_s()
      if len(idspectrum_s) > 0:
        output("Starting...")
        no = len(idspectrum_s)
        i = 0
        ii = 0
        for idspectrum in idspectrum_s:
          #curve = t_series.get_curve_1spectrum(idspectrum)
          jg_s[i_jg].idspectrum = idspectrum # the judge object is responsible for 
          jg_s[i_jg].make_judgement()
          
          t_spectrum_judge.insert({
          "params": jg_s[i_jg].judgement.get_params(), 
          "idjudge": idjudge_s[i_jg], 
          "idspectrum": idspectrum, 
          "idexperiment": session.idexperiment
          })
          
          i += 1
          ii += 1
          if ii == 500:
            progress(float(i+1)/no)
            ii = 0

        progress(1)
        output("...done.")
    except Exception, e:
      output("* ERROR: "+str(e.message)+"; ", OUTPUT_ERROR)
      raise
    finally:
      pass


      
    
    

def train(idjudge_train, idjudge_reference):
  cl_train = t_judge.get_judge_from_id(idjudge_train)
  cl_reference = t_judge.get_judge_from_id(idjudge_reference)
