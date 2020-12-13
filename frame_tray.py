#Boa:Frame:frame_tray

import wx
import wx.grid

def create(parent):
    return frame_tray(parent)

[wxID_FRAME_TRAY, wxID_FRAME_TRAYGRIDSAMPLE, wxID_FRAME_TRAYGRIDSLIDE, wxID_FRAME_TRAYGRIDTRAY, wxID_FRAME_TRAYPANEL1, wxID_FRAME_TRAYPANEL2, 
 wxID_FRAME_TRAYPANEL3, wxID_FRAME_TRAYSTATICTEXT1, wxID_FRAME_TRAYSTATICTEXT2, wxID_FRAME_TRAYSTATICTEXT3, 
] = [wx.NewId() for _init_ctrls in range(10)]

class frame_tray(wx.Frame):
  def _init_coll_boxSizerBody_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panel1, 10, border=10, flag=wx.GROW)
    parent.AddWindow(self.panel2, 16, border=0, flag=wx.GROW)
    parent.AddWindow(self.panel3, 26, border=0, flag=wx.GROW)

  def _init_coll_boxSizer3_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText3, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.gridSample, 1, border=0, flag=wx.GROW)

  def _init_coll_boxSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.gridTray, 1, border=0, flag=wx.GROW)

  def _init_coll_boxSizer2_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText2, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.gridSlide, 1, border=0, flag=wx.GROW)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizerBody = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer2 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer3 = wx.BoxSizer(orient=wx.VERTICAL)

    self._init_coll_boxSizerBody_Items(self.boxSizerBody)
    self._init_coll_boxSizer1_Items(self.boxSizer1)
    self._init_coll_boxSizer2_Items(self.boxSizer2)
    self._init_coll_boxSizer3_Items(self.boxSizer3)

    self.SetSizer(self.boxSizerBody)
    self.panel1.SetSizer(self.boxSizer1)
    self.panel2.SetSizer(self.boxSizer2)
    self.panel3.SetSizer(self.boxSizer3)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Frame.__init__(self, id=wxID_FRAME_TRAY, name='frame_tray', parent=prnt, pos=wx.Point(461, 226), size=wx.Size(550, 426),
      style=wx.DEFAULT_FRAME_STYLE, title='Trays, slides, colonys')
    self.SetClientSize(wx.Size(534, 390))
    self.SetToolTipString('frame_tray')

    self.panel1 = wx.Panel(id=wxID_FRAME_TRAYPANEL1, name='panel1', parent=self, pos=wx.Point(0, 0), size=wx.Size(534, 75), style=wx.TAB_TRAVERSAL)

    self.panel2 = wx.Panel(id=wxID_FRAME_TRAYPANEL2, name='panel2', parent=self, pos=wx.Point(0, 75), size=wx.Size(534, 120), style=wx.TAB_TRAVERSAL)

    self.panel3 = wx.Panel(id=wxID_FRAME_TRAYPANEL3, name='panel3', parent=self, pos=wx.Point(0, 195), size=wx.Size(534, 195), style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_FRAME_TRAYSTATICTEXT1, label='Trays', name='staticText1', parent=self.panel1, pos=wx.Point(0, 0),
      size=wx.Size(534, 13), style=0)

    self.gridTray = wx.grid.Grid(id=wxID_FRAME_TRAYGRIDTRAY, name='gridTray', parent=self.panel1, pos=wx.Point(0, 13), size=wx.Size(534, 62), style=0)

    self.staticText2 = wx.StaticText(id=wxID_FRAME_TRAYSTATICTEXT2, label='Slides in tray', name='staticText2', parent=self.panel2, pos=wx.Point(0,
      0), size=wx.Size(534, 13), style=0)

    self.gridSlide = wx.grid.Grid(id=wxID_FRAME_TRAYGRIDSLIDE, name='gridSlide', parent=self.panel2, pos=wx.Point(0, 13), size=wx.Size(534, 107),
      style=0)

    self.staticText3 = wx.StaticText(id=wxID_FRAME_TRAYSTATICTEXT3, label='Samples in slide', name='staticText3', parent=self.panel3, pos=wx.Point(0,
      0), size=wx.Size(534, 13), style=0)

    self.gridSample = wx.grid.Grid(id=wxID_FRAME_TRAYGRIDSAMPLE, name='gridSample', parent=self.panel3, pos=wx.Point(0, 13), size=wx.Size(534, 182),
      style=0)

    self._init_sizers()

  def init_grids(self):
    #self.gridTray.EnableEditing(False)
    #self.gridTray.SetSelectionMode(wx.grid.Grid.wxGridSelectRows)
    pass


  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_grids()
