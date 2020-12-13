"""Report3 is the Maps report (the one that exports annotated trays and slides as JPG)"""
import db_con, html, act_main, wx
from session import session
from table_colony import t_colony
from table_tray import t_tray
from table_spectrum import t_spectrum
from table_slide import t_slide
from output import *
from errors import *
from table_setup import t_setup
import os, cStringIO
import wx.lib.floatcanvas.FloatCanvas as fc
from pair import *      
from misc import *

class html_r3(html.html):
  def _styles(self):
    html.html._styles(self)
    self.add("""
<style>\n
    .title1 {font-size: 22x; font-weight: bold; padding: 10px; background-color: #e0e0e0; border-bottom: 1px solid black; border-left: 3px solid black; }
    .title2 {font-size: 20x; font-weight: bold; padding: 7px 7px 7px 10px; background-color: #f0f0f0; border-bottom: 1px solid black; border-left: 3px solid black; }
    .title3 {font-size: 20x; text-align: center; font-weight: bold; padding: 5px; text-decoration: underline; }
    .td_def { border: 1px solid black; vertical-align: top; padding: 10px;}\n
    .p_def {padding-left: 10px; }
\n
</style>
""")

  def open_td(self, w=None):
    """Added a valign=top to try to make Openoffice understand this. It does!"""
    self.add("<td valign=top class=td_def"+(w and " width="+str(w) or "")+">")

  def open_table(self):
    self.add("<table border=1 cellpadding=7px width=100%>")



def adjust_canvas(canvas, factor=1):
  """Hack over FloatCanvas to make it resize properly"""
  canvas._ResetBoundingBox()
  bb = canvas.BoundingBox
  canvas.SetSize(wx.Size(abs(bb[0, 0]-bb[1, 0])*factor, abs(bb[0, 1]-bb[1, 1])*factor))
  # FloatCanvas starts a timer in its OnTimer event handler, but we cannot wait.
  # The following lines have been copied from FloatCanvas.OnSizeTimer()
  canvas.MakeNewBuffers()
  canvas.ZoomToBB()


#-------------------------------------------------------------------------------
#---- THE REPORT ---------------------------------------------------------------
#-------------------------------------------------------------------------------
def generate(idtray_s, minimum_spectra):
  """A lot of effort has been made to make it look pretty inside Openoffice document with minimal alterations."""
 
  try: 
    dlg = wx.FileDialog(None, 'Save report as', t_setup.get_value("path_html"), '', '*.html', wx.SAVE)
   
    if dlg.ShowModal() == wx.ID_OK:
      file_name = dlg.GetPath()
      dir_name = os.path.dirname(file_name)
      t_setup.update({"path_html": dir_name})
    
      # Report beginning
      h = html_r3(output_type=html.OUTPUT_FILE, file_name=file_name)
      h.open()
      h.page_header("Maps - Trays and Slides")
      
      w = wx.Frame(None)
      
      for idtray in idtray_s:

        (tray_code, tray_comments, tray_picture) = t_tray.get_values_from_id(("code", "comments", "picture"), idtray)

        data_slide = t_slide.get_cursor_1tray(("id", "code", "shapes", "picture", "comments"), idtray).fetchall()
        no_slides = len(data_slide)


        h.raw("<br>")
        h.title1("Tray "+tray_code)

        ###############
        # Tray details
        
        if tray_comments:
          h.p(tray_comments)

        if tray_picture <> None:
          canvas = fc.FloatCanvas(parent=w, id=wx.NewId())
  
          img = wx.ImageFromStream(cStringIO.StringIO(tray_picture), wx.BITMAP_TYPE_ANY)
          canvas.AddScaledBitmap(img.ConvertToBitmap(), (0, 0), Position="tl", Height=img.GetHeight())
          
          file_name = tray_code+".jpg"
          complete_file_name = os.path.join(dir_name, file_name)

          
          for i in range(0, no_slides):
            slide_code = data_slide[i][1]
            slide_shapes = data_slide[i][2]
            
            p = pairs()
            p.from_string(slide_shapes, slide_code)
            
            for pair in p.pairs:
              canvas.AddObject(pair.shape)
              canvas.AddObject(pair.text) 
          
          adjust_canvas(canvas)

          canvas.SaveAsImage(complete_file_name, ImageType=wx.BITMAP_TYPE_JPEG)
          
          h.open_p_center()

          TRAY_W = 500
          bb = canvas.BoundingBox
          height =  int(TRAY_W*abs(bb[0, 1]-bb[1, 1])/abs(bb[0, 0]-bb[1, 0]))
                
          h.img(file_name, w=str(TRAY_W)+"px", h=str(height)+"px")
          h.close_p()
          
        # Slides details
        
        if no_slides > 0:
          NO_COLS = 3
          SLIDE_W = 165
          col = 0
          flag_first = True
          
          h.raw("<br>")
          h.title1("Tray "+tray_code+" Slides")

          for (idslide, slide_code, slide_shapes, slide_picture, slide_comments) in data_slide:
            if col == 0:
              if not flag_first:
                h.close_tr()
                h.close_table()
                h.raw("<br>")
              else:
                flag_first = False
              h.open_table()
              h.open_tr()
            col += 1
            if col == NO_COLS:
              col = 0
              
            h.open_td(w=str(int(100/NO_COLS))+"%")

            h.title3(slide_code)

            
            # Slide details

            if slide_picture <> None:
              canvas = fc.FloatCanvas(parent=w, id=wx.NewId())

              img = wx.ImageFromStream(cStringIO.StringIO(slide_picture), wx.BITMAP_TYPE_ANY)
              canvas.AddScaledBitmap(img.ConvertToBitmap(), (0, 0), Position="tl", Height=img.GetHeight())
              
              file_name = slide_code+".jpg"
              complete_file_name = os.path.join(dir_name, file_name)

              data_colony = t_spectrum.get_cursor_data(field_names=(
              "colony.code", 
              "colony.shapes", 
              "colony.comments", 
              "sum(flag_inactive is null or flag_inactive = 0) as sum_active",
              ),
              groupbys=["colony.id"], flag_join_slide=True, iddeact=session.iddeact, idslide=idslide).fetchall()

              
              
              no_colonies = len(data_colony)
              
              for i in range(0, no_colonies):
                colony_code = data_colony[i][0]
                colony_shapes = data_colony[i][1]
                spectrum_count = data_colony[i][3]
                
                if spectrum_count >= minimum_spectra:
                  p = pairs()
                  p.from_string(colony_shapes, code_in_canvas(colony_code, slide_code))
                  
                  for pair in p.pairs:
                    canvas.AddObject(pair.shape)
                    canvas.AddObject(pair.text) 
              
              adjust_canvas(canvas)

              canvas.SaveAsImage(complete_file_name, ImageType=wx.BITMAP_TYPE_JPEG)
              
              h.open_p_center()

              bb = canvas.BoundingBox
              height =  int(SLIDE_W*abs(bb[0, 1]-bb[1, 1])/abs(bb[0, 0]-bb[1, 0]))

              h.img(file_name, w=str(SLIDE_W)+"px", h=str(height)+"px")
              h.close_p()

            if slide_comments:
              h.p(slide_comments)
            
            for i in range(0, no_colonies):
              spectrum_count = data_colony[i][3]
                
              if spectrum_count >= minimum_spectra:
                colony_code = data_colony[i][0]
                colony_comments = data_colony[i][2]
                if colony_comments:
                  h.raw(colony_code+" - "+colony_comments+"<br>")
            
            h.close_td()
        
        if not flag_first:
          h.close_tr()
          h.close_table()

      
      
#      h.open_table()
      
      # table header
#      h.open_tr()
#      h.th("Tray", 50)
#      h.th("Slide", 50)
#      h.th("Colony", 50)
#      h.th("File name", 50)
      
#      for name in judge_names(idtray_s):
#        h.th(name, 50)

#      h.close_tr()


#      i = 0
#      ii = 0
#      colony_code_last = -1
#      for row in data:
        # row is (idspectrum, flag_active, tray code, slide code, colony code, file name, ...)

#        h.open_tr()
#        for value in row[NO_COLS_SKIP:]:
#          h.td(value)
#        h.close_tr()
        
#        i += 1
#        ii += 1
#        if ii == 123:
#          progress(float(i+1)/rows)
#          ii = 0

#      progress(1)
      
#      h.close_table()

      h.close()


  
  except error_x, e:
    act_main.handle_error(e)
