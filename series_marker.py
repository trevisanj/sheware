import wx
import wx.lib.floatcanvas.FloatCanvas as fc
import table
import numpy as N
from marker import *
from series import *
from errors import *


class event_series_marker(event_series):
  index = -1

class series_marker(series):
  """Does not draw lines but puts triangles, lines, circles, or generally, markers where there are points."""

  marker_type = MARKER_STAR
  marker_size = 1
  colors = None # Used to paint each marker with one different color.


  def draw_data(self):
    """The event to be eventually passed to a binder function will contain an index attribute indicating the position in the data vectors"""
    width = self.flag_selected and 3 or 1
    
    m = marker()
    m.fc = self.fc
    m.line_width = width
    m.color = self.color
    m.type = self.marker_type
    m.size = self.marker_size
    
    flag_colors = self.colors != None
    
    i = 0
    for (x, y) in self.datac:
      if flag_colors:
        m.color = self.colors[i]
      m.draw(x, y)
      for sh in m.shapes:
        event = event_series_marker()
        event.index = i
        self.add_shape(sh, event)
      i += 1
          
    #print self.datac
  
  
class series3d_marker(series3d):
  """Implementation is identical to series_marker. Maybe it is possible to use multiple inheritance to avoid repetition. TODO"""

  marker_type = MARKER_STAR
  marker_size = 1
  colors = None # Used to paint each marker with one different color.


  def draw_data(self):
    """The event to be eventually passed to a binder function will contain an index attribute indicating the position in the data vectors"""
    width = self.flag_selected and 3 or 1
    
    m = marker()
    m.fc = self.fc
    m.line_width = width
    m.color = self.color
    m.type = self.marker_type
    m.size = self.marker_size
    
    flag_colors = self.colors != None
    
    i = 0
    for (x, y) in self.datac:
      if flag_colors:
        m.color = self.colors[i]
      m.draw(x, y)
      for sh in m.shapes:
        event = event_series_marker()
        event.index = i
        self.add_shape(sh, event)
      i += 1
          
    #print self.datac
  