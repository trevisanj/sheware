#Boa:Dialog:DialogReport3
import wx, wx.grid, db_con, session, act_report2

from table_colony import t_colony
from table_judge import t_judge
from table_score import t_score
from table_colony_judge import t_colony_judge
from table_tray import t_tray
from output import *
from session import *

def create(parent):
    return DialogReport3(parent)

[wxID_DIALOGREPORT3, wxID_DIALOGREPORT3BUTTONGENERATE, wxID_DIALOGREPORT3CHECKLISTBOX, wxID_DIALOGREPORT3PANEL1, wxID_DIALOGREPORT3STATICTEXT1, 
 wxID_DIALOGREPORT3STATICTEXTCLASSIFIER, wxID_DIALOGREPORT3TEXTCTRLMINIMUMSPECTRA, 
] = [wx.NewId() for _init_ctrls in range(7)]

class DialogReport3(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticTextClassifier, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.checkListBox, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText1, 0, border=0, flag=0)
    parent.AddWindow(self.textCtrlMinimumSpectra, 0, border=0, flag=0)

  def _init_coll_boxSizerBody_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panel1, 1, border=0, flag=wx.GROW)
    parent.AddWindow(self.buttonGenerate, 0, border=10, flag=wx.ALIGN_BOTTOM | wx.ALL)

  def _init_coll_flexGridSizer1_Growables(self, parent):
    # generated method, don't edit

    parent.AddGrowableRow(1)
    parent.AddGrowableCol(1)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizerBody = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.flexGridSizer1 = wx.FlexGridSizer(cols=2, hgap=0, rows=2, vgap=0)

    self._init_coll_boxSizerBody_Items(self.boxSizerBody)
    self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
    self._init_coll_flexGridSizer1_Growables(self.flexGridSizer1)

    self.SetSizer(self.boxSizerBody)
    self.panel1.SetSizer(self.flexGridSizer1)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGREPORT3, name='DialogReport3', parent=prnt, pos=wx.Point(510, 290), size=wx.Size(487, 256),
      style=wx.DEFAULT_FRAME_STYLE, title='Experiment maps')
    self.SetClientSize(wx.Size(471, 220))
    self.SetToolTipString('DialogTray')

    self.panel1 = wx.Panel(id=wxID_DIALOGREPORT3PANEL1, name='panel1', parent=self, pos=wx.Point(0, 0), size=wx.Size(355, 220),
      style=wx.TAB_TRAVERSAL)
    self.panel1.SetMinSize(wx.Size(534, 83))

    self.staticTextClassifier = wx.StaticText(id=wxID_DIALOGREPORT3STATICTEXTCLASSIFIER, label='Trays to figure in report',
      name='staticTextClassifier', parent=self.panel1, pos=wx.Point(5, 5), size=wx.Size(115, 13), style=0)

    self.checkListBox = wx.CheckListBox(choices=[], id=wxID_DIALOGREPORT3CHECKLISTBOX, name='checkListBox', parent=self.panel1, pos=wx.Point(133, 5),
      size=wx.Size(217, 171), style=0)

    self.buttonGenerate = wx.Button(id=wxID_DIALOGREPORT3BUTTONGENERATE, label='&Generate report', name='buttonGenerate', parent=self,
      pos=wx.Point(365, 187), size=wx.Size(96, 23), style=0)
    self.buttonGenerate.Bind(wx.EVT_BUTTON, self.OnButtonGenerateButton, id=wxID_DIALOGREPORT3BUTTONGENERATE)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGREPORT3STATICTEXT1, label='Minimum active spectra per colony', name='staticText1',
      parent=self.panel1, pos=wx.Point(0, 181), size=wx.Size(128, 35), style=0)

    self.textCtrlMinimumSpectra = wx.TextCtrl(id=wxID_DIALOGREPORT3TEXTCTRLMINIMUMSPECTRA, name='textCtrlMinimumSpectra', parent=self.panel1,
      pos=wx.Point(128, 181), size=wx.Size(32, 21), style=0, value='4')

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_choices()


  def init_choices(self):
    self.data_tray = t_tray.get_cursor_1experiment(("id", "code"), session.idexperiment).fetchall()
    for (id, code) in self.data_tray:
      self.checkListBox.Append(code)
   


  def OnButtonGenerateButton(self, event):
    
    
    idtray_s = []
    for i in range(0, len(self.data_tray)):
      if self.checkListBox.IsChecked(i):
        idtray_s.append(self.data_tray[i][0])

    if len(idtray_s) == 0:
      output.output("No trays were selected.", OUTPUT_ERROR)
      return
    
    minimum_spectra = int(self.textCtrlMinimumSpectra.GetValue())

    import act_report3
    act_report3.generate(idtray_s, minimum_spectra)
    

    


