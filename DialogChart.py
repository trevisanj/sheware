#Boa:Dialog:DialogChart

import wx
import wx.lib.floatcanvas.FloatCanvas as fc
import wx.lib.floatcanvas.NavCanvas as nc

from session import session

def create(parent):
    return DialogChart(parent)

[wxID_DIALOGCHART, wxID_DIALOGCHARTPANELCHART, 
] = [wx.NewId() for _init_ctrls in range(2)]

wxID_NC = wx.NewId()

class DialogChart(wx.Dialog):
  def _init_coll_boxSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panelChart, 10, border=5, flag=wx.GROW | wx.ALL)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerChart = wx.BoxSizer(orient=wx.VERTICAL)

    self._init_coll_boxSizer1_Items(self.boxSizer1)

    self.SetSizer(self.boxSizer1)
    self.panelChart.SetSizer(self.boxSizerChart)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGCHART, name='DialogChart', parent=prnt, pos=wx.Point(14, 14), size=wx.Size(1114, 767),
      style=wx.DEFAULT_FRAME_STYLE, title='Chart')
    self.SetClientSize(wx.Size(1098, 731))
    self.Bind(wx.EVT_ACTIVATE, self.OnDialogChartActivate)
    self.Bind(wx.EVT_CLOSE, self.OnDialogChartClose)
    self.Bind(wx.EVT_SIZE, self.OnDialogChartSize)
    self.Bind(wx.EVT_MAXIMIZE, self.OnDialogChartMaximize)

    self.panelChart = wx.Panel(id=wxID_DIALOGCHARTPANELCHART, name='panelChart', parent=self, pos=wx.Point(5, 5), size=wx.Size(1088, 721),
      style=wx.TAB_TRAVERSAL)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_nc(parent)


  def init_nc(self, prnt):
    
      
    self.nc = nc.NavCanvas(id=wxID_NC, parent=self.panelChart)
    #self.nc.Bind(wx.EVT_KEY_DOWN, OnCanvasKeyDown)
    self.canvas = self.nc.Canvas
    #self.canvas.Bind(wx.EVT_KEY_DOWN, OnCanvasKeyDown)

    #self.canvas.Bind(wx.EVT_MOTION, self.OnPanelPictureMotion)

    self.boxSizerChart.AddWindow(self.nc, 1, border=1, flag=wx.ALL | wx.GROW)

    self.panelChart.Layout()

  def OnDialogChartActivate(self, event):
    self.flag_start_now = 1
    self.lets_see_what()
    

  def lets_see_what(self):
    if self.flag_start_now:
      self.populate_all()
      self.ch.draw()


  def populate_all(self):
    from misc import chart_from_colony

    if self.idcolony: 
      self.ch = chart_from_colony(self.idcolony, self.idspectrum_selected)
      self.ch.fc = self.canvas


  def OnDialogChartClose(self, event):
    self.ch.undraw()
    event.Skip()

  def OnDialogChartSize(self, event):
    self.canvas.ZoomToBB()
    event.Skip()

  def OnDialogChartMaximize(self, event):
    self.canvas.ZoomToBB()
    event.Skip()
    
