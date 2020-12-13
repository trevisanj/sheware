#Boa:Dialog:DialogEditExperiment

import wx
import act_main
from output import *
from errors import *
from table_experiment import t_experiment

def create(parent):
    return DialogEditExperiment(parent)

[wxID_DIALOGEDITEXPERIMENT, wxID_DIALOGEDITEXPERIMENTBUTTONCANCEL, wxID_DIALOGEDITEXPERIMENTBUTTONOK, wxID_DIALOGEDITEXPERIMENTPANELBOTTOM, 
 wxID_DIALOGEDITEXPERIMENTPANELCLIENT, wxID_DIALOGEDITEXPERIMENTSTATICTEXT1, wxID_DIALOGEDITEXPERIMENTSTATICTEXT2, 
 wxID_DIALOGEDITEXPERIMENTSTATICTEXT3, wxID_DIALOGEDITEXPERIMENTTEXTCTRLCOMMENTS, wxID_DIALOGEDITEXPERIMENTTEXTCTRLID, 
 wxID_DIALOGEDITEXPERIMENTTEXTCTRLNAME, 
] = [wx.NewId() for _init_ctrls in range(11)]

class DialogEditExperiment(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlId, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText2, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlName, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText3, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.textCtrlComments, 0, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizerBottomPanel_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonOk, 1, border=10, flag=wx.ALL | wx.ALIGN_RIGHT)
    parent.AddWindow(self.buttonCancel, 1, border=10, flag=wx.ALL | wx.ALIGN_RIGHT)

  def _init_coll_flexGridSizer1_Growables(self, parent):
    # generated method, don't edit

    parent.AddGrowableCol(1)

  def _init_coll_boxSizerFrame_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panelClient, 1, border=0, flag=wx.GROW)
    parent.AddWindow(self.panelBottom, 0, border=0, flag=wx.GROW)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizerFrame = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerBottomPanel = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.flexGridSizer1 = wx.FlexGridSizer(cols=2, hgap=0, rows=3, vgap=0)

    self._init_coll_boxSizerFrame_Items(self.boxSizerFrame)
    self._init_coll_boxSizerBottomPanel_Items(self.boxSizerBottomPanel)
    self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
    self._init_coll_flexGridSizer1_Growables(self.flexGridSizer1)

    self.SetSizer(self.boxSizerFrame)
    self.panelBottom.SetSizer(self.boxSizerBottomPanel)
    self.panelClient.SetSizer(self.flexGridSizer1)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGEDITEXPERIMENT, name='DialogEditExperiment', parent=prnt, pos=wx.Point(421, 301), size=wx.Size(543, 222),
      style=wx.DEFAULT_DIALOG_STYLE, title='Experiment')
    self.SetClientSize(wx.Size(527, 186))
    self.Center(wx.BOTH)

    self.panelBottom = wx.Panel(id=wxID_DIALOGEDITEXPERIMENTPANELBOTTOM, name='panelBottom', parent=self, pos=wx.Point(0, 143), size=wx.Size(527, 43),
      style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGEDITEXPERIMENTBUTTONOK, label='&Ok', name='buttonOk', parent=self.panelBottom, pos=wx.Point(10, 10),
      size=wx.Size(243, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton, id=wxID_DIALOGEDITEXPERIMENTBUTTONOK)

    self.buttonCancel = wx.Button(id=wxID_DIALOGEDITEXPERIMENTBUTTONCANCEL, label='&Cancel', name='buttonCancel', parent=self.panelBottom,
      pos=wx.Point(273, 10), size=wx.Size(243, 23), style=0)
    self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton, id=wxID_DIALOGEDITEXPERIMENTBUTTONCANCEL)

    self.panelClient = wx.Panel(id=wxID_DIALOGEDITEXPERIMENTPANELCLIENT, name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(527, 143),
      style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGEDITEXPERIMENTSTATICTEXT1, label='Id', name='staticText1', parent=self.panelClient, pos=wx.Point(5,
      9), size=wx.Size(11, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGEDITEXPERIMENTSTATICTEXT2, label='Name', name='staticText2', parent=self.panelClient,
      pos=wx.Point(5, 40), size=wx.Size(55, 13), style=0)

    self.staticText3 = wx.StaticText(id=wxID_DIALOGEDITEXPERIMENTSTATICTEXT3, label='Comments', name='staticText3', parent=self.panelClient,
      pos=wx.Point(5, 95), size=wx.Size(55, 13), style=0)

    self.textCtrlId = wx.TextCtrl(id=wxID_DIALOGEDITEXPERIMENTTEXTCTRLID, name='textCtrlId', parent=self.panelClient, pos=wx.Point(70, 5),
      size=wx.Size(100, 21), style=0, value='')
    self.textCtrlId.Enable(False)

    self.textCtrlName = wx.TextCtrl(id=wxID_DIALOGEDITEXPERIMENTTEXTCTRLNAME, name='textCtrlName', parent=self.panelClient, pos=wx.Point(70, 36),
      size=wx.Size(452, 21), style=0, value='')

    self.textCtrlComments = wx.TextCtrl(id=wxID_DIALOGEDITEXPERIMENTTEXTCTRLCOMMENTS, name='textCtrlComments', parent=self.panelClient,
      pos=wx.Point(70, 67), size=wx.Size(452, 70), style=wx.TE_MULTILINE, value='')

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.result = wx.ID_CANCEL

  def set_mode(self, mode):
    if mode == "insert":
      self.SetTitle("Insert experiment")
    elif mode == "edit":
      self.SetTitle("Edit experiment")
    else:
      raise error_x("Invalid mode: %s." % mode)
    self.mode = mode
    
    
  def set_id(self, value):
    self.textCtrlId.SetValue(str(value))

    row = t_experiment.get_values_from_id(("id", "name", "comments"), value)
    self.set_name(row[1])
    self.set_comments(row[2])

  def get_id(self):
    return self.textCtrlId.GetValue()

    
  def set_name(self, value):
    self.textCtrlName.SetValue(str(value))
  def get_name(self):
    return self.textCtrlName.GetValue()
    
  def set_comments(self, value):
    self.textCtrlComments.SetValue(str(value))     
  def get_comments(self):
    return self.textCtrlComments.GetValue()
    
    

  def OnButtonOkButton(self, event):
    try:
      #Consistency
      
      name = self.get_name()
      if len(name) == 0:
        raise error_x("Please inform name.")
      comments = self.get_comments()
      d = {"name": name, "comments": comments}
      
      if self.mode == "edit":
        t_experiment.update(d, self.get_id())
      else:
        t_experiment.insert(d)

      self.result = wx.ID_OK
      self.Close()
    except error_x, e:
      output(e.message, OUTPUT_ERROR, True)
  

  def OnButtonCancelButton(self, event):
      self.Close()
