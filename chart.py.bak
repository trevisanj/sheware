import wx
import wx.lib.floatcanvas.FloatCanvas as fc
import table
import numpy as np
from series import *
from errors import *

class chart(object):

  color_axis = "#aaaaaa"

  # Device context boundaries
  xc_min = 0
  xc_max = 1618
  yc_min = 0
  yc_max = 1000

  # Data boundaries
  x_min = -1
  x_max = -1
  y_min = -1
  y_max = -1

  # Custom boundaries. If informed, they are forced to be used!
  custom_x_min = None
  custom_x_max = None
  custom_y_min = None
  custom_y_max = None

  flag_calculated = False
  flag_children_instructed = False
  flag_drawn = False

  __fc = None
  
  def set_fc(self, value):
    self.__fc = value
    self.flag_children_instructed = False
  

  def __init__(self):
    self.seriess = []
    self.axes = []
    
  
  def bind_series(self, series):
    self.seriess.append(series)
    series.chart = self
    self.flag_calculated = False
    self.flag_children_instructed = False
    
  def unbind_series(self, series):
    series.chart = None
    self.seriess.remove(series)


  def bind_axis(self, axis):
    self.axes.append(axis)
    axis.chart = self
    self.flag_children_instructed = False
    
  def unbind_axis(self, axis):
    axis.chart = None
    self.axes.remove(axis)

  def assure_calculated(self):
    if not self.flag_calculated:
      self.calc_boundaries()
      self.flag_calculated = True

  def assure_children_instructed(self):
    if not self.flag_children_instructed:  
      for series in self.seriess+self.axes:
        self.instruct_child(series)
      self.flag_children_instructed = True
  
  def calc_boundaries(self):
    print "olha o seriesssssssssssssssss tem"
    print len(self.seriess)
    if len(self.seriess) > 0:
      self.x_max = self.custom_x_max or max(map(lambda(series): len(series.x_values) > 0 and max(series.x_values) or 1, self.seriess))
      self.x_min = self.custom_x_min or min(map(lambda(series): len(series.x_values) > 0 and min(series.x_values) or 0, self.seriess))

      self.y_max = self.custom_y_max or max(map(lambda(series): len(series.y_values) > 0 and max(series.y_values) or 1, self.seriess))
      self.y_min = self.custom_y_min or min(map(lambda(series): len(series.y_values) > 0 and min(series.y_values) or 0, self.seriess))
    else:
      self.x_max = 1
      self.x_min = 0
      self.y_max = 1
      self.y_min = 0
      
  def instruct_child(self, series):
    series.fc = self.fc
    
    series.x_min = self.x_min
    series.x_max = self.x_max
    series.y_min = self.y_min
    series.y_max = self.y_max
    
    series.xc_min = self.xc_min
    series.xc_max = self.xc_max
    series.yc_min = self.yc_min
    series.yc_max = self.yc_max
  

  
  def assure_undrawn(self):
    if self.flag_drawn:
      self.undraw()
      self.flag_drawn = False
  
  def draw(self):
    self.assure_undrawn()
    self.assure_calculated()
    self.make_axes()
    self.assure_children_instructed()
    
    for series in self.axes+self.seriess:
      series.draw()
    
    self.fc.ZoomToBB()
    self.flag_drawn = True
    #self.fc.Draw(Force=True)

    
  def undraw(self):
    self.fc.ClearAll()
    for series in self.seriess+self.axes:
      series.shapes = []
      series.undraw()
    self.fc.Draw(Force=True)


  def clear(self):
    """Undraws and deletes all series"""
    
    self.undraw()
    self.seriess = []
    self.axes = []
    

  def make_axes(self):
    # Axes!
    
    # x
    se = series()
    se.color = self.color_axis
    self.bind_axis(se)
    se.x_values = np.array([self.x_min, self.x_max, self.x_max, self.x_min, self.x_min])
    se.y_values = np.array([self.y_min, self.y_min, self.y_max, self.y_max, self.y_min])
    
    if self.y_min < 0 and self.y_max > 0:
      se = series()
      se.color = self.color_axis
      self.bind_axis(se)
      se.x_values = np.array([self.x_min, self.x_max])
      se.y_values = np.array([0, 0])
      

    


#---------------------#---------------------#---------------------#---------------------#---------------------#---------------------    
    
class chart3d(chart):
  
  # Device context boundaries
  xc_min = 0
  xc_max = 1000
  yc_min = 0
  yc_max = 1000

  # Data boundaries
  z_min = -1
  z_max = -1

  # Custom boundaries. If informed, they are forced to be used!
  custom_z_min = None
  custom_z_max = None


  __alpha = 0
  __beta = 0
  __gamma = 0
  

  def set_alpha(self, value):
    self.__alpha = value
    self.__flag_angles_passed = False
    
  alpha = property(fget=lambda(self): self.__alpha, fset=set_alpha)  
  
  def set_beta(self, value):
    self.__beta = value
    self.__flag_angles_passed = False
    
  beta = property(fget=lambda(self): self.__beta, fset=set_beta)  
  
  def set_gamma(self, value):
    self.__gamma = value
    self.__flag_angles_passed = False
    
  gamma = property(fget=lambda(self): self.__gamma, fset=set_gamma)


  def calc_boundaries(self):
    chart.calc_boundaries(self)

    self.z_max = self.custom_z_max or max(map(lambda(series): max(series.z_values), self.seriess))
    self.z_min = self.custom_z_min or min(map(lambda(series): min(series.z_values), self.seriess))

    div = len(self.seriess)*len(self.seriess[0].x_values)

    self.x_center = sum(map(lambda(series): sum(series.x_values), self.seriess))/div
    self.y_center = sum(map(lambda(series): sum(series.y_values), self.seriess))/div
    self.z_center = sum(map(lambda(series): sum(series.z_values), self.seriess))/div


  def instruct_child(self, series):
    chart.instruct_child(self, series)

    series.z_min = self.z_min
    series.z_max = self.z_max
    
    series.x_center = self.x_center
    series.y_center = self.y_center
    series.z_center = self.z_center
      
    series.alpha = self.__alpha
    series.beta = self.__beta
    series.gamma = self.__gamma

  
  
  def make_axes(self):
    # Axes!
    
    # 20 is because the axis drawings (or polylines ) are about 20 units long
    # 3 is because we want small axes
    div = 20/max([abs(x) for x in (self.x_min-self.x_center, self.x_max-self.x_center, 
        self.y_min-self.y_center, self.y_max-self.y_center, self.z_min-self.z_center, self.z_max-self.z_center)])*3
    
    # x
    se = series3d()
    se.color = self.color_axis
    self.bind_axis(se)
    se.x_values = np.array([0, 20, 19, 19, 20])/div+self.x_center
    se.y_values = np.array([0, 0, 1, -1, 0])/div+self.y_center
    se.z_values = np.array([0, 0, 0, 0, 0])

    # y
    se = series3d()
    se.color = self.color_axis
    self.bind_axis(se)
    se.x_values = np.array([0, 0, 1, 1, -1])/div+self.x_center
    se.y_values = np.array([0, 20, 19, 21, 19])/div+self.y_center
    se.z_values = np.array([0, 0, 0, 0, 0])
    
    # z
    se = series3d()
    se.color = self.color_axis
    self.bind_axis(se)
    se.x_values = np.array([0, 0, -1, -1])/div+self.x_center
    se.y_values = np.array([0, 0, 0, 0])
    se.z_values = np.array([0, 20, 19, 20])/div+self.z_center


