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

NO_COLS_SKIP = 1 # Number of cols before tray.code in data returned by mount_data()

def mount_data(idjudge_s):
  #orderbys = ("colony.code", "spectrum.file_name");
  orderbys = ("spectrum.file_name", );
  
  data = []
  
  

  clss = len(idjudge_s)
  data1 = t_spectrum.get_cursor_data(field_names=
      ("(flag_inactive is null or flag_inactive = 0) as flag_active",
       "spectrum.id", 
       "tray.code as tray_code", 
       "slide.code as slide_code", 
       "colony.code as colony_code", 
       "spectrum.file_name"
      ), 
      idexperiment=session.idexperiment,
      orderbys=orderbys,
      iddeact=session.iddeact,
      flag_join_tray=True,
      idjudge_s=idjudge_s).fetchall()
  data = map(list, data1)

#  data_more = []
#  for idjudge in idjudge_s:
#    data_more.append(t_spectrum.get_cursor_data(idjudge_s=[idjudge], idexperiment=session.idexperiment, iddeact=session.iddeact, 
#    orderbys=orderbys).fetchall())

  # Mounts a list of judgement objects
  judgements = []
  for class_name in judge_class_names(idjudge_s):
    j = judge_object(class_name)
    judgements.append(j.judgement_object())
  
  
    #l = []
    
  # This loop replaces the last columns, of content e.g. 'code="A"', by a convenient interpretation e.g. "A"
  for j in range(0, clss):
    for i_row in range(0, len(data1)):

      # data_more is a list of 2-d lists ((idspectrum, params), ...) which comes from table_spectrum.get_cursor_joined_params()

      judgements[j].init_params()
      judgements[j].set_params(data1[i_row][-clss+j])
      data[i_row][-clss+j] = judgements[j].get_default_value()
      
      #print "oooooooooooooooooooooooooooodefaultvalue "+str(judgements[j].get_default_value())

#    i += 1
    
  return data

def judge_class_names(ids):
  result = []
  for id_ in ids:
    result.append(t_judge.get_value_from_id("class_name", id_))
  
  return result  
  
def judge_names(ids):
  result = []
  for id_ in ids:
    result.append(t_judge.get_value_from_id("name", id_))
  
  return result  

def generate(idjudge_s):
 
  try: 
    dlg = wx.FileDialog(None, 'Save report as', t_setup.get_value("path_html"), '', '*.html', wx.SAVE)
   
    if dlg.ShowModal() == wx.ID_OK:
      file_name = dlg.GetPath()
      t_setup.update({"path_html": os.path.dirname(file_name)})
    
      data = mount_data(idjudge_s)  

      # Report beginning
      rows = len(data)
      clss = len(idjudge_s)
      
      h = html.html(output_type=html.OUTPUT_FILE, file_name=file_name)
      h.open()
      h.page_header("Classified spectrums")
      
      h.open_table()
      
      # table header
      h.open_tr()
      h.th("Tray", 50)
      h.th("Slide", 50)
      h.th("Colony", 50)
      h.th("File name", 50)
      
      for name in judge_names(idjudge_s):
        h.th(name, 50)

      h.close_tr()


      i = 0
      ii = 0
      colony_code_last = -1
      for row in data:
        # row is (idspectrum, flag_active, tray code, slide code, colony code, file name, ...)

        h.open_tr()
        for value in row[NO_COLS_SKIP:]:
          h.td(value)
        h.close_tr()
        
        i += 1
        ii += 1
        if ii == 123:
          progress(float(i+1)/rows)
          ii = 0

      progress(1)
      
      h.close_table()
      h.close()


  
  except error_x, e:
    act_main.handle_error(e)
