
def paint_grid_row(colour, grid, row_no):
  """Paints a wxGrid row"""
  
  for col_no in range(0, grid.GetNumberCols()):
    grid.SetCellBackgroundColour(row_no, col_no, colour)
  
  grid.Refresh()
  

def code_in_canvas(colony_code, slide_code):  
  "Subtracts slide_code from colony_code if the contents of the latter contains that of the former in its beginning"
  
  l = len(slide_code)

  if colony_code[0:l] == slide_code:
    return colony_code[l:]
  else:
    return colony_code

def vector2str(vector):
  # old  return "["+",".join(map(str, vector))+"]"
  return " ".join(map(str, vector))


def str2vector(s):
  return map(float, s.split(" "))

def chart_from_colony(idcolony, idspectrum_selected=None):
  "returns a chart object given a colony id"
  from session import session
  from chart import chart
  from series import series
  
  from table_spectrum import t_spectrum
  data = t_spectrum.get_cursor_data(field_names=("spectrum.id", "spectrum.idcolony", "series.vector", "flag_inactive"), \
      iddomain=session.iddomain, idcolony=idcolony, idexperiment=session.idexperiment, iddeact=session.iddeact)

  ch = chart()

  i = 0
  for (idspectrum, idcolony, vector, flag_inactive) in data:
    se = series()
    if vector == None:
      se.y_values = []
    else:
      se.y_values = str2vector(vector)
      
    se.color = session.get_spectrum_color(i)
    if not flag_inactive:
      pass
    else:
      se.line_style = "Dot"
    if idspectrum_selected and idspectrum == idspectrum_selected:
      se.flag_selected = True
    ch.bind_series(se)
    
    i += 1
    
  return ch