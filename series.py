import wx
import wx.lib.floatcanvas.FloatCanvas as fc
import table
import numpy as np
from errors import *
from math import sin, cos
import traceback
import sys

class event_series(object):
  shape = None

class series(object):


  def assure_ready_to_draw(self):
    if self.xc_min == -1:
      raise error_x("Boundaries not set.")
    
    if self.__chart == None:
      raise error_x("Chart not set.")
  
  def __init__(self):
    self.__x_values = None
    self.__y_values = []
    self.__flag_selected = False
    self.__color = "#000000"
    self.__line_style = "Solid"
    self.__flag_selected = False
    self.__chart = None

    # Device context boundaries
    self.xc_min = -1
    self.xc_max = -1
    self.yc_min = -1
    self.yc_max = -1
    
    # Data boundaries
    self.x_min = -1
    self.x_max = -1
    self.y_min = -1
    self.y_max = -1

    # Binder function: it is called whenever a new shape is added to the canvas. The purpose is to perform eventual mouse events (or whatever) bindings to the shape
    self.binder_function = None
    

    self.flag_redraw = False
    self.flag_sh = False
    self.fc = None
    self.shapes = []

    
  def set_chart(self, chart):
    self.__chart = chart
      
  chart = property(fget=lambda(self): self.__chart, fset=set_chart)
    
    
  def set_y_values(self, values):
    """If data is set before x_values, a default 0-based, 1-spaced x_values will be generated"""
    self.__y_values = values
    
#    print "olholholholholholholholholholholholholholholholholholholholholholholholholholho"
#    print values
#    traceback.print_list(traceback.extract_stack())
#    print '---------------------------------------------------------------------------------------------------------------'
    
    if self.__x_values == None:
      self.__x_values = range(0, len(values))
    self.flag_redraw = True
      
  data = property(lambda(self): self.__y_values, set_y_values)
  y_values = property(lambda(self): self.__y_values, set_y_values)
  
  def set_x_values(self, values):
    self.__x_values = values
    self.flag_redraw = True
      
  x_values = property(lambda(self): self.__x_values, set_x_values)
  
  def set_color(self, color):
    self.__color = color
    self.flag_redraw = True
  
  color = property(lambda(self): self.__color, set_color)
  
  def set_line_style(self, line_style):
    self.__line_style = line_style
    self.flag_redraw = True
  
  line_style = property(lambda(self): self.__line_style, set_line_style)

  def set_flag_selected(self, flag_selected):
    self.__flag_selected = flag_selected
    self.flag_redraw = True
  
  flag_selected = property(lambda(self): self.__flag_selected, set_flag_selected)

  
  def undraw(self):
    if self.flag_sh:
      #for sh in self.shapes:
      #  self.fc.RemoveObject(sh)
      #self.sh = None
      self.flag_sh = False
      self.shapes = []

  def calc_xc(self, x):
    return float(x-self.x_min)/(self.x_max-self.x_min)*(self.xc_max-self.xc_min)+self.xc_min

  def calc_yc(self, y):
    return (y-self.y_min)/(self.y_max-self.y_min)*(self.yc_max-self.yc_min)+self.yc_min
  
  def calc_datac(self):
    """Calculates the data for the canvas"
    
    In the future, initial x will be something else"""
    datac = []
    
    i = 0
    print "nooooooooooooooooooooooooooooossa mano"
    print self.x_values
    print self.y_values
    for y in self.y_values:
      x = self.__x_values[i]
      i += 1
      
      datac.append((self.calc_xc(x), self.calc_yc(y)))
      
    self.datac = datac
  
  def redraw(self):
    if self.flag_redraw:
      self.draw()
      self.flag_redraw = False
  
  def draw(self):
    self.assure_ready_to_draw()
    self.calc_datac()

    try:  
      self.draw_data()
    finally:
      self.flag_sh = len(self.shapes) > 0
      
    #print self.datac
    
  def add_shape(self, sh, event=event_series()):
    self.shapes.append(sh)
    self.fc.AddObject(sh)
    event.shape = sh
    if self.binder_function:
      self.binder_function(event)

  

  def draw_data(self):
    if len(self.datac) > 0:
      w = self.__flag_selected and 3 or 1  
      
      self.add_shape(fc.Line(self.datac, LineColor = self.__color, LineWidth=w, LineStyle=self.__line_style))
  
  
  
#----------------------#----------------------#----------------------#----------------------#----------------------#----------------------

class series3d(series):
  
  def __init__(self):
    series.__init__(self)
    
    self.__x_values = []
    self.__y_values = []
    self.__z_values = []

    # Device context boundaries
    self.zc_min = -1
    self.zc_max = -1
    
    # Data boundaries
    self.z_min = -1
    self.z_max = -1
    
  __flag_rotation_ok = False
  __alpha = 0
  __beta = 0
  __gamma = 0
  rotation_matrix = None
  
  def set_alpha(self, value):
    self.__alpha = value
    self.__flag_rotation_ok = False
    
  alpha = property(fget=lambda(self): self.__alpha, fset=set_alpha)  
  
  def set_beta(self, value):
    self.__beta = value
    self.__flag_rotation_ok = False
    
  beta = property(fget=lambda(self): self.__beta, fset=set_beta)  
  
  def set_gamma(self, value):
    self.__gamma = value
    self.__flag_rotation_ok = False
    
  gamma = property(fget=lambda(self): self.__gamma, fset=set_gamma)


    
  def set_x_values(self, values):
    self.__x_values = values
    self.flag_redraw = True

  x_values = property(lambda(self): self.__x_values, set_x_values)
    
  def set_y_values(self, values):
    self.__y_values = values
    self.flag_redraw = True

  y_values = property(lambda(self): self.__y_values, set_y_values)
    
  def set_z_values(self, values):
    self.__z_values = values
    self.flag_redraw = True

  z_values = property(lambda(self): self.__z_values, set_z_values)
  
  def calc_xc(self, x):
    return float(x-self.x_min)/(self.x_max-self.x_min)*(self.xc_max-self.xc_min)+self.xc_min

  def calc_yc(self, y):
    return (y-self.y_min)/(self.y_max-self.y_min)*(self.yc_max-self.yc_min)+self.yc_min
  
  
  def calculate_rotation_matrix(self):
    a = self.alpha
    b = self.beta
    c = self.gamma
    self.rotation_matrix = np.array(
      [[cos(b)*cos(c),                       -cos(b)*sin(c),                      sin(b)],
       [sin(a)*sin(b)*cos(c)+cos(a)*sin(c),  -sin(a)*sin(b)*sin(c)+cos(a)*cos(c), -sin(a)*cos(b)],
       [-cos(a)*sin(b)*cos(c)+sin(a)*sin(c), cos(a)*sin(b)*sin(c)+sin(a)*cos(c),  cos(a)*cos(b)]
      ])
         
  def assure_rotation_ok(self):
    if not self.__flag_rotation_ok:
      self.calculate_rotation_matrix()
      self.__flag_rotation_ok = True


  def calc_xc(self, x):
    return float(x-self.x_min)/(self.x_max-self.x_min)*(self.xc_max-self.xc_min)+self.xc_min

  def calc_yc(self, y):
    """Scaling is the same of x. This is a try to avoid deformation."""
    return (y-self.y_min)/(self.x_max-self.x_min)*(self.xc_max-self.xc_min)+self.yc_min

  
  
  def calc_datac(self):
    """Calculates the data for the canvas"""
    
    self.assure_rotation_ok()
    
    datac = []
    
    for i in range(0, len(self.__x_values)):
      x = self.__x_values[i]
      y = self.__y_values[i]
      z = self.__z_values[i]
      i += 1
      
      v0 = np.array([x-self.x_center, y-self.y_center, z-self.z_center])
      (x1, y1, z1) = np.dot(self.rotation_matrix, v0)
            
      
      datac.append((self.calc_xc(x1), self.calc_yc(y1)))

    self.datac = datac
  
