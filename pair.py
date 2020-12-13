import wx
import wx.lib.floatcanvas.FloatCanvas as fc
import table
import numpy as N
from errors import *

class pairs(object):
  """This class represents a list of pair objects. This list corresponds either to one slide or one colony."""


  def __init__(self, table = None, id_ = None, caption = ""):
    self.pairs = []
    self.table = table
    self.id_ = id_
    self.caption = caption

  # There is not a load() method because a SELECT statement can be used to load many pair sets from the database.
  # from_string() can be called the counterpart to save().
  #
  # In the other hand, only one pair set can be saved at a time.
  def save(self):
    """Saves pair to database."""
    assert isinstance(self.table, table.table)
    assert isinstance(self.id_,(int, long))
    
    self.table.update({"shapes": self.to_string()}, self.id_)

  def to_string(self):
    """Mounts a string of lines returned by pair.to_string()."""
    return "\n".join(map(lambda(pair): pair.to_string(), self.pairs))

  def from_string(self, s, caption):
    """Populates self.pairs"""
    
    if len(self.pairs) > 0:
      raise error_x("Cannot populate. Non-empty pair set.")
    
    if s == None:
      s = ""
    
    for line in s.split("\n"):
      if len(line) > 0:
        o_pair = pair()
        self.pairs.append(o_pair)
      
        o_pair.from_string(line, caption)
      




shape_styles = {
  "active": {"LineColor": "#FF0000", "LineStyle": "Solid", "LineWidth": 3, "FillColor": None, "FillStyle": "Solid"},
  "inactive": {"LineColor": "#900000", "LineStyle": "Solid", "LineWidth": 2, "FillColor": None, "FillStyle": "Solid"},
  "defining": {"LineColor": "#FF8000", "LineStyle": "LongDash", "LineWidth": 3, "FillColor": None, "FillStyle": "Solid"}, 
  "selected": {"LineColor": "#FF8000", "LineStyle": "Solid", "LineWidth": 4, "FillColor": None, "FillStyle": "CrossHatch"}
  }

FONT_SIZE = 18

###########################################################################################################

class pair(object):
  """This class represents a tuple (floatcanvas.Rectangle/Ellipse, floatCanvas.Text), where the second is a legend to the firts."""
  
  shape = None
  text = None

  def get_text_left_top(self):
    """Calculates text (left, top) according to shape position."""
    YOFF = 1
    (x, y) = self.shape.XY
    (w, h) = self.shape.WH
    
    left = x+w/2
    if h < 0: top = y+YOFF
    else: top = y+h+YOFF
    
    return (left, top)    

  def change_text_xy(self, xy):
    self.text.XY = N.array(xy, N.float)
    self.text.XY.shape = (2,)
    self.text.CalcBoundingBox()

  def change_xywh(self, xy, wh):
    self.shape.SetShape(xy, wh)
    self.change_text_xy(self.get_text_left_top())

  def create_text(self, caption):
    "Creates a floatcanvas.Text control with calculated position (over shape)."""
    
    self.text = fc.ScaledText(caption, self.get_text_left_top(), Size =  FONT_SIZE, Color = "Black", BackgroundColor = "#B0B0B0", Family = wx.SWISS, Style = wx.NORMAL,
      Weight = wx.BOLD, Underlined = False, Position = 'bc', InForeground = False, Font = None)
  
  def to_string(self):
    """Mounts a line containing "rec, 10, 10, 20, 10" or "ell, 20, 412, 23, 12", where the numbers stand for (left, top, width, height)"""
    sh = self.shape
    return ",".join((isinstance(sh, fc.Rectangle) and "rec" or "ell", 
                     str(sh.XY[0]), 
                     str(sh.XY[1]), 
                     str(sh.WH[0]), 
                     str(sh.WH[1])
                    ))
                    
  def from_string(self, line, caption):
    (shape_type, left, top, width, height) = line.split(",")

    if (shape_type == "rec"):
      f = self.rectangle
    else:
      f = self.ellipse
    
    f((left, top), (width, height), caption)
    self.configure_style("inactive")

  def configure_style(self, how):
    d = shape_styles[how]
    
    o = self.shape
    o.LineColor = d["LineColor"]
    o.LineStyle = d["LineStyle"]
    o.LineWidth = d["LineWidth"]
    o.FillColor = d["FillColor"]
    o.FillStyle = d["FillStyle"]
    o.HitLineWidth = max(o.LineWidth, o.MinHitLineWidth)
    o.SetPen(o.LineColor, o.LineStyle, o.LineWidth)
    o.SetBrush(o.FillColor, o.FillStyle)

    self.text.Color = d["LineColor"]
        
  def rectangle(self, xy, wh, s):
    self.shape = fc.Rectangle(xy, wh)
    self.shape.pair = self
    self.create_text(s)
    
  def ellipse(self, xy, wh, s):
    self.shape = fc.Ellipse(xy, wh)
    self.shape.pair = self
    self.create_text(s)
