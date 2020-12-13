#Boa:Dialog:DialogPCA

import wx
import wx.lib.floatcanvas.FloatCanvas as fc
import wx.lib.floatcanvas.NavCanvas as nc

from spectrum_lot import spectrum_lot
from pca_lot import pca_lot
from chart import *
from series_marker import *
from chart import *
from series_marker import *
from session import *
from table_spectrum import t_spectrum
from table_judge import t_judge
from output import *
from sentence_lot import sentence_lot
import math

COLORS = ["#000000", "#f00000", "#00f000", "#0000f0", "#af00ad", "#e38b00", "#00585e", "#db3c70", "#72a76e", "#407675"]


def create(parent):
    return DialogPCA(parent)

[wxID_DIALOGPCA, wxID_DIALOGPCABUTTON1, wxID_DIALOGPCABUTTON2, wxID_DIALOGPCABUTTON3, wxID_DIALOGPCABUTTON4, wxID_DIALOGPCABUTTON5, 
 wxID_DIALOGPCABUTTON6, wxID_DIALOGPCABUTTONCALCULATE, wxID_DIALOGPCABUTTONEIGENVALUES, wxID_DIALOGPCABUTTONLOADINGS, wxID_DIALOGPCABUTTONSHOW, 
 wxID_DIALOGPCACHOICEDIMENSIONS, wxID_DIALOGPCACHOICEJUDGE, wxID_DIALOGPCAPANEL3DCONTROLS, wxID_DIALOGPCAPANELPCA, wxID_DIALOGPCAPANELTOP, 
 wxID_DIALOGPCASTATICTEXT1, wxID_DIALOGPCASTATICTEXT2, wxID_DIALOGPCASTATICTEXT3, wxID_DIALOGPCASTATICTEXTANGLES, 
 wxID_DIALOGPCASTATICTEXTDIMENSIONS, wxID_DIALOGPCASTATICTEXTMARKERSIZE, wxID_DIALOGPCASTATICTEXTSEQ, wxID_DIALOGPCATEXTCTRLMARKERSIZE, 
 wxID_DIALOGPCATEXTCTRLSEQ, 
] = [wx.NewId() for _init_ctrls in range(25)]

wxID_NC = wx.NewId()

class DialogPCA(wx.Dialog):
  def _init_coll_boxSizer3DControls_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.button1, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.button2, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.button3, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.button4, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.button5, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.button6, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticTextAngles, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)

  def _init_coll_boxSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panelTop, 0, border=0, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.panel3DControls, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.panelPCA, 10, border=5, flag=wx.GROW | wx.ALL)

  def _init_coll_boxSizer2_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonCalculate, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticTextDimensions, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.choiceDimensions, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticTextSeq, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlSeq, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticTextMarkerSize, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlMarkerSize, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText2, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.choiceJudge, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText3, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.buttonEigenvalues, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.buttonShow, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.buttonLoadings, 0, border=5, flag=wx.ALL)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerPCA = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer2 = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.boxSizer3DControls = wx.BoxSizer(orient=wx.HORIZONTAL)

    self._init_coll_boxSizer1_Items(self.boxSizer1)
    self._init_coll_boxSizer2_Items(self.boxSizer2)
    self._init_coll_boxSizer3DControls_Items(self.boxSizer3DControls)

    self.SetSizer(self.boxSizer1)
    self.panelPCA.SetSizer(self.boxSizerPCA)
    self.panelTop.SetSizer(self.boxSizer2)
    self.panel3DControls.SetSizer(self.boxSizer3DControls)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGPCA, name='DialogPCA', parent=prnt, pos=wx.Point(1312, 2), size=wx.Size(1104, 578),
      style=wx.DEFAULT_FRAME_STYLE, title='PCA')
    self.SetClientSize(wx.Size(1088, 542))
    self.Center(wx.BOTH)
    self.Bind(wx.EVT_ACTIVATE, self.OnDialogPCAActivate)
    self.Bind(wx.EVT_CLOSE, self.OnDialogPCAClose)
    self.Bind(wx.EVT_SIZE, self.OnDialogPCASize)
    self.Bind(wx.EVT_MAXIMIZE, self.OnDialogPCAMaximize)

    self.panelPCA = wx.Panel(id=wxID_DIALOGPCAPANELPCA, name='panelPCA', parent=self, pos=wx.Point(5, 81), size=wx.Size(1078, 456),
      style=wx.TAB_TRAVERSAL)

    self.panelTop = wx.Panel(id=wxID_DIALOGPCAPANELTOP, name='panelTop', parent=self, pos=wx.Point(0, 0), size=wx.Size(1088, 33),
      style=wx.TAB_TRAVERSAL)

    self.buttonCalculate = wx.Button(id=wxID_DIALOGPCABUTTONCALCULATE, label='&Calculate', name='buttonCalculate', parent=self.panelTop,
      pos=wx.Point(5, 5), size=wx.Size(75, 23), style=0)
    self.buttonCalculate.Bind(wx.EVT_BUTTON, self.OnButtonCalculateButton, id=wxID_DIALOGPCABUTTONCALCULATE)

    self.buttonEigenvalues = wx.Button(id=wxID_DIALOGPCABUTTONEIGENVALUES, label='&Eigenvalues', name='buttonEigenvalues', parent=self.panelTop,
      pos=wx.Point(775, 5), size=wx.Size(73, 23), style=0)
    self.buttonEigenvalues.Bind(wx.EVT_BUTTON, self.OnButtonEigenvaluesButton, id=wxID_DIALOGPCABUTTONEIGENVALUES)

    self.staticTextSeq = wx.StaticText(id=wxID_DIALOGPCASTATICTEXTSEQ, label='PC sequence', name='staticTextSeq', parent=self.panelTop,
      pos=wx.Point(205, 10), size=wx.Size(63, 13), style=0)

    self.buttonShow = wx.Button(id=wxID_DIALOGPCABUTTONSHOW, label='&Scores', name='buttonShow', parent=self.panelTop, pos=wx.Point(858, 5),
      size=wx.Size(75, 23), style=0)
    self.buttonShow.Bind(wx.EVT_BUTTON, self.OnButtonShowButton, id=wxID_DIALOGPCABUTTONSHOW)

    self.textCtrlSeq = wx.TextCtrl(id=wxID_DIALOGPCATEXTCTRLSEQ, name='textCtrlSeq', parent=self.panelTop, pos=wx.Point(278, 5), size=wx.Size(70, 21),
      style=0, value='0, 1, 2')

    self.staticTextDimensions = wx.StaticText(id=wxID_DIALOGPCASTATICTEXTDIMENSIONS, label='Dimensions', name='staticTextDimensions',
      parent=self.panelTop, pos=wx.Point(90, 10), size=wx.Size(55, 13), style=0)

    self.choiceDimensions = wx.Choice(choices=["2D", "3D"], id=wxID_DIALOGPCACHOICEDIMENSIONS, name='choiceDimensions', parent=self.panelTop,
      pos=wx.Point(155, 5), size=wx.Size(40, 21), style=0)

    self.staticTextMarkerSize = wx.StaticText(id=wxID_DIALOGPCASTATICTEXTMARKERSIZE, label='Marker size', name='staticTextMarkerSize',
      parent=self.panelTop, pos=wx.Point(358, 10), size=wx.Size(55, 13), style=0)

    self.textCtrlMarkerSize = wx.TextCtrl(id=wxID_DIALOGPCATEXTCTRLMARKERSIZE, name='textCtrlMarkerSize', parent=self.panelTop, pos=wx.Point(423, 5),
      size=wx.Size(22, 21), style=0, value='3')

    self.panel3DControls = wx.Panel(id=wxID_DIALOGPCAPANEL3DCONTROLS, name='panel3DControls', parent=self, pos=wx.Point(5, 38), size=wx.Size(1078,
      33), style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGPCASTATICTEXT1, label='3D controls: Alt+...', name='staticText1', parent=self.panel3DControls,
      pos=wx.Point(5, 10), size=wx.Size(94, 13), style=0)

    self.button1 = wx.Button(id=wxID_DIALOGPCABUTTON1, label='&1 - X CCW', name='button1', parent=self.panel3DControls, pos=wx.Point(109, 5),
      size=wx.Size(75, 23), style=0)
    self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wxID_DIALOGPCABUTTON1)

    self.button2 = wx.Button(id=wxID_DIALOGPCABUTTON2, label='&2 - X CW', name='button2', parent=self.panel3DControls, pos=wx.Point(194, 5),
      size=wx.Size(75, 23), style=0)
    self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button, id=wxID_DIALOGPCABUTTON2)

    self.button3 = wx.Button(id=wxID_DIALOGPCABUTTON3, label='&3 - Y CCW', name='button3', parent=self.panel3DControls, pos=wx.Point(279, 5),
      size=wx.Size(75, 23), style=0)
    self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button, id=wxID_DIALOGPCABUTTON3)

    self.button4 = wx.Button(id=wxID_DIALOGPCABUTTON4, label='&4 - Y CW', name='button4', parent=self.panel3DControls, pos=wx.Point(364, 5),
      size=wx.Size(75, 23), style=0)
    self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button, id=wxID_DIALOGPCABUTTON4)

    self.button5 = wx.Button(id=wxID_DIALOGPCABUTTON5, label='&5 - Z CCW', name='button5', parent=self.panel3DControls, pos=wx.Point(449, 5),
      size=wx.Size(75, 23), style=0)
    self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button, id=wxID_DIALOGPCABUTTON5)

    self.button6 = wx.Button(id=wxID_DIALOGPCABUTTON6, label='&6 - Z CW', name='button6', parent=self.panel3DControls, pos=wx.Point(534, 5),
      size=wx.Size(75, 23), style=0)
    self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button, id=wxID_DIALOGPCABUTTON6)

    self.choiceJudge = wx.Choice(choices=[], id=wxID_DIALOGPCACHOICEJUDGE, name='choiceJudge', parent=self.panelTop, pos=wx.Point(559, 5),
      size=wx.Size(130, 21), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGPCASTATICTEXT2, label='Classes come from', name='staticText2', parent=self.panelTop,
      pos=wx.Point(455, 10), size=wx.Size(94, 13), style=0)

    self.staticTextAngles = wx.StaticText(id=wxID_DIALOGPCASTATICTEXTANGLES, label='Angles', name='staticTextAngles', parent=self.panel3DControls,
      pos=wx.Point(619, 10), size=wx.Size(55, 13), style=0)
    self.staticTextAngles.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'MS Shell Dlg 2'))

    self.staticText3 = wx.StaticText(id=wxID_DIALOGPCASTATICTEXT3, label='What to plot', name='staticText3', parent=self.panelTop, pos=wx.Point(699,
      10), size=wx.Size(66, 13), style=0)

    self.buttonLoadings = wx.Button(id=wxID_DIALOGPCABUTTONLOADINGS, label='&Loadings', name='buttonLoadings', parent=self.panelTop, pos=wx.Point(943,
      5), size=wx.Size(75, 23), style=0)
    self.buttonLoadings.Bind(wx.EVT_BUTTON, self.OnButtonLoadingsButton, id=wxID_DIALOGPCABUTTONLOADINGS)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_nc(parent)
    self.init_choices()

    if len(self.data_cl) > 0:
      self.choiceDimensions.SetSelection(0)

    self.set_flag_calculated(False)
    self.set_flag_scores_plot(False)


  def init_nc(self, prnt):
    
      
    self.nc = nc.NavCanvas(id=wxID_NC, parent=self.panelPCA)
    #self.nc.Bind(wx.EVT_KEY_DOWN, OnCanvasKeyDown)
    self.canvas = self.nc.Canvas
    #self.canvas.Bind(wx.EVT_KEY_DOWN, OnCanvasKeyDown)

    #self.canvas.Bind(wx.EVT_MOTION, self.OnPanelPictureMotion)

    self.boxSizerPCA.AddWindow(self.nc, 1, border=1, flag=wx.ALL | wx.GROW)

    self.panelPCA.Layout()


  def init_choices(self):
    self.data_cl = t_judge.get_all_data(("id", "name"))
    for (id, name) in self.data_cl:
      self.choiceJudge.Append(name)


  def set_flag_calculated(self, value):
    self.flag_calculated = value
    self.sync_calculated()

  def set_flag_scores_plot(self, value):
    self.flag_scores_plot = value
    self.sync_scores_plot()

  def sync_calculated(self):
    self.buttonEigenvalues.Enabled = self.flag_calculated
    self.buttonShow.Enabled = self.flag_calculated
    self.buttonLoadings.Enabled = self.flag_calculated

  def sync_scores_plot(self):
    
    # Enables/disables 3D controls
    flag_sinequanon = self.flag_calculated and self.get_dimensions() == 1
    self.panel3DControls.Enabled = flag_sinequanon and self.flag_scores_plot


  def OnDialogPCAActivate(self, event):
    event.Skip()

  def OnDialogPCAClose(self, event):
    event.Skip()

  def OnDialogPCASize(self, event):
    self.canvas.ZoomToBB()
    event.Skip()

  def OnDialogPCAMaximize(self, event):
    self.canvas.ZoomToBB()
    event.Skip()

  def clear_canvas(self):
    self.canvas.ClearAll()
    self.canvas.Draw(Force=True)

  def configure_object(self, o):
    o.idexperiment = session.idexperiment
    o.iddomain = session.iddomain
    o.iddeact = session.iddeact
    o.flag_active_only = True

  def OnButtonCalculateButton(self, event):
    "Loads spectra and calculates the PCA."

    self.set_flag_calculated(False)

    self.o1 = spectrum_lot()
    o1 = self.o1
    self.configure_object(o1)
    o1.read()

    self.o2 = pca_lot()
    o2 = self.o2
    o2.spectrum_lot = o1
    o2.calculate()

    self.set_flag_calculated(True)
    

  def OnButtonEigenvaluesButton(self, event):
    self.clear_canvas()
    ch = chart()
    ch.fc = self.canvas
    
    
    se = series()
    ch.bind_series(se)
    se.color = "#000000"
    se.data = self.o2.eigenvals
    
    ch.draw()

  def get_pc(self, ctrl, s):
    try:
      pc = int(ctrl.GetValue())
    except:
      raise error_x("Invalid integer value for %s!" % s)
    if not pc in range(0, self.o1.wncount):
      raise error_x("%s must be between 0 and %s!" % (s, self.o1.wncount-1))
    return pc


  def get_pc_s(self):
    s = self.textCtrlSeq.GetValue()
    try:
      pc_s = [int(x) for x in s.split(",")]
    except ValueError, e:
      raise error_x(e.message)
    return pc_s


  def get_marker_size(self):
    ctrl = self.textCtrlMarkerSize
    s = "marker size"
    try:
      value = int(ctrl.GetValue())
    except:
      raise error_x("Invalid integer value for %s!" % s)
    return value


  def get_idjudge(self):
    index = self.choiceJudge.GetSelection()
    if index < 0:
      return -1
    return self.data_cl[index][0]

  def get_dimensions(self):
    """0 - 2D; 1 - 3D"""
    index = self.choiceDimensions.GetSelection()
    return index
  

  def on_shape_down(self, obj):
    import DialogEditSpectrum
    dlg = DialogEditSpectrum.create(None)
    dlg.set_id(self.o1.by_index[obj.spectrum_index][0])
    try:
      dlg.ShowModal()
    finally:
      #pass
      dlg.Destroy()

    #

  def OnButtonShowButton(self, event):
    def binder_function(event2):
      event2.shape.spectrum_index = event2.index
      event2.shape.Bind(fc.EVT_FC_LEFT_DOWN, self.on_shape_down)      
      
    
    pc_s = self.get_pc_s()
    ms = self.get_marker_size()
    idjudge = self.get_idjudge()
    
    flag_judge = False
    if idjudge > 0:
      self.sl = sentence_lot()
      sl = self.sl
      self.configure_object(sl)
      sl.colors = COLORS
      sl.idjudge = idjudge
      sl.read()
      sl.calculate()

      flag_judge = True
      


    
    
    self.clear_canvas()
    
    if self.get_dimensions() == 0:
      if len(pc_s) < 2:
        raise error_x("At least 2 PC's are needed!")
      
      x_pc = pc_s[0]
      y_pc = pc_s[1]
      
      ch = chart()
      ch.fc = self.canvas
      
      se = series_marker()
      ch.bind_series(se)
      se.marker_size = ms
      se.binder_function = binder_function
      se.x_values = self.o2.scores[:, x_pc]
      se.y_values = self.o2.scores[:, y_pc]
      
    else:
      if len(pc_s) < 3:
        raise error_x("At least 3 PC's are needed!")

      x_pc = pc_s[0]
      y_pc = pc_s[1]
      z_pc = pc_s[2]
      
      ch = chart3d()
      self.ch = ch
      ch.fc = self.canvas
      
      se = series3d_marker()
      ch.bind_series(se)
      se.marker_size = ms
      se.binder_function = binder_function
      se.x_values = self.o2.scores[:, x_pc]
      se.y_values = self.o2.scores[:, y_pc]
      se.z_values = self.o2.scores[:, z_pc]
      
    
    if flag_judge:
      se.colors = sl.get_colors()    

    if self.get_dimensions() == 0:
      ch.draw()
    else:
      self.redraw_3d()
    
    
    self.set_flag_scores_plot(True)
      

  def redraw_3d(self):
    self.ch.alpha = self.alpha_deg*math.pi/180
    self.ch.beta = self.beta_deg*math.pi/180
    self.ch.gamma = self.gamma_deg*math.pi/180
    
    self.ch.draw()

    self.staticTextAngles.SetLabel("alpha = %s ; beta = %s ; gamma = %s" % (self.alpha_deg, self.beta_deg, self.gamma_deg))



    
  alpha_deg = 0
  beta_deg = 0
  gamma_deg = 0
  
  ANGLE_INCREMENT = 22.5 # in degrees

  def inc_alpha(self, by):
    self.alpha_deg += by
    self.redraw_3d()

  def inc_beta(self, by):
    self.beta_deg += by
    self.redraw_3d()

  def inc_gamma(self, by):
    self.gamma_deg += by
    self.redraw_3d()

  def OnButton1Button(self, event):
    self.inc_alpha(self.ANGLE_INCREMENT)

  def OnButton2Button(self, event):
    self.inc_alpha(-self.ANGLE_INCREMENT)
    
  def OnButton3Button(self, event):
    self.inc_beta(self.ANGLE_INCREMENT)
    
  def OnButton4Button(self, event):
    self.inc_beta(-self.ANGLE_INCREMENT)

  def OnButton5Button(self, event):
    self.inc_gamma(self.ANGLE_INCREMENT)

  def OnButton6Button(self, event):
    self.inc_gamma(-self.ANGLE_INCREMENT)

  def OnButtonLoadingsButton(self, event):
    self.clear_canvas()
    ch = chart()
    ch.custom_y_max = 1.
    ch.custom_y_min = -1.
    ch.fc = self.canvas
    
    pc_s = self.get_pc_s()
    i = 0
    for pc in pc_s:    
      se = series()
      ch.bind_series(se)
      se.color = COLORS[i]
      se.data = self.o2.get_loading(pc)
      
      i += 1
    
    ch.draw()

