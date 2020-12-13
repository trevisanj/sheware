import db_con, html, act_main, wx
from session import session
from table_colony import t_colony
from table_judge import t_judge
from table_spectrum import t_spectrum
from table_spectrum_judge import t_spectrum_judge
from output import *
from errors import *
from table_setup import t_setup
from judge import *
import os

def get_data(idcl):
  return t_spectrum.get_cursor_joined_params(idjudge=idcl, idexperiment=session.idexperiment).fetchall()
  

def generate(idcl, idcls):
 
  try: 
    dlg = wx.FileDialog(None, 'Save report as', t_setup.get_value("path_html"), '', '*.html', wx.SAVE)
   
    if dlg.ShowModal() == wx.ID_OK:
      file_name = dlg.GetPath()
      t_setup.update({"path_html": os.path.dirname(file_name)})
    

      data1 = get_data(idcl)
      data_more = []
      for idcl_ in idcls:
        data_more.append(get_data(idcl_))
    
  
      # Mounts a dict to find judge names ...
      data_cl = t_judge.get_all_data(("id", "name", "class_name"))
      dict_judge = {}
      for row in data_cl:
        dict_judge[row[0]] = row[1:3]
        
      # ... and a list of judgement objects as well ...
      judgements = []
      for idcl_ in idcls:
        j = judge_object(dict_judge[idcl_][1])
        judgements.append(j.judgement_object())


      # ... and the reference judge
      j1 = judge_object(dict_judge[idcl][1])
      judgement1 = j1.judgement_object()
      

      # Report beginning
      rows = len(data1)
      clss = len(idcls)
      
      print rows, len(data_more[0])

      
      h = html.html(output_type=html.OUTPUT_FILE, file_name=file_name)
      h.open()
      h.page_header("Comparison")
      h.subtitle("Reference judge: "+dict_judge[idcl][0])
      
      h.open_table()
      
      # table header
      h.open_tr()
      h.th("Classifier name", 200)
      h.th("% Concordance", 100)
      h.close_tr()


      i_cl = 0
      for idcl_ in idcls:
        h.open_tr()
        h.td(dict_judge[idcl_][0])
        
        
        count_eq = 0 # counts equalities
        
        for row1, row2 in zip(data1, data_more[i_cl]):
          (d1, params1) = row1
          (d3, params2) = row2
          
          judgement1.set_params(params1)
          judgements[i_cl].set_params(params2)
         
          count_eq = count_eq+(judgement1.compare_to(judgements[i_cl]))

        
        h.td(str(float(count_eq)/rows*100)+"%")
        
        h.close_tr()
        
        
        i_cl += 1
        
      
      h.close_table()
      h.close()


  
  except error_x, e:
    act_main.handle_error(e)
