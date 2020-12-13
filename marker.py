import wx
import wx.lib.floatcanvas.FloatCanvas as fc
import table
import numpy as N
from errors import *
import math

MARKER_TRIANGLE = 0
MARKER_STAR = 1


class marker(object):
  """Draws markers (like points, stars, triangles etc centered in coordinates"""

  color = "#000000"
  line_width = 1
  type = MARKER_STAR
  fc = None
  size = 1

  def make_points(self, angles):
    """angles in degrees."""
    points = []
    for angle in angles:
      in_rad = angle/180.*math.pi
      points.append((self.x+self.size*math.cos(in_rad), self.y+self.size*math.sin(in_rad)))
    self.points = points
  
  
  def draw(self, x=None, y=None):
    """Draws marker and stores shapes just created."""
    self.shapes = []
    
    if x <> None:
      self.x = x
    if y <> None:
      self.y = y
    
    if self.type == MARKER_STAR:
      self.make_points((90, 234, 378, 522, 666, 810))
    elif self.type == MARKER_TRIANGLE:
      self.make_points((90, 210, 360, 480))
      
    sh = fc.Line(self.points, LineColor = self.color, LineWidth=self.line_width)
    self.shapes.append(sh)
    self.fc.AddObject(sh)
  
  