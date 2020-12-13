#Boa:Dialog:DialogSelX

import wx
from output import *
from errors import *
from session import session
from table_experiment import t_experiment

def create(parent):
    return DialogSelX(parent)

[wxID_DIALOGSELX, wxID_DIALOGSELXBUTTONCANCEL, wxID_DIALOGSELXBUTTONOK, wxID_DIALOGSELXCHOICEEXPERIMENT, wxID_DIALOGSELXPANELBOTTOM, 
 wxID_DIALOGSELXPANELCLIENT, wxID_DIALOGSELXSTATICTEXTEXPERIMENT, 
] = [wx.NewId() for _init_ctrls in range(7)]

class DialogSelX(wx.Dialog):
  def _init_coll_flexGridSizerBody_Growables(self, parent):
    # generated method, don't edit

    parent.AddGrowableCol(1)

  def _init_coll_boxSizerBottomPanel_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonOk, 1, border=10, flag=wx.ALL | wx.ALIGN_RIGHT)
    parent.AddWindow(self.buttonCancel, 1, border=10, flag=wx.ALL | wx.ALIGN_RIGHT)

  def _init_coll_flexGridSizerBody_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticTextExperiment, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.choiceExperiment, 0, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizerFrame_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panelClient, 1, border=40, flag=wx.GROW)
    parent.AddWindow(self.panelBottom, 0, border=40, flag=wx.GROW)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizerFrame = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerBottomPanel = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.flexGridSizerBody = wx.FlexGridSizer(cols=3, hgap=5, rows=1, vgap=5)

    self._init_coll_boxSizerFrame_Items(self.boxSizerFrame)
    self._init_coll_boxSizerBottomPanel_Items(self.boxSizerBottomPanel)
    self._init_coll_flexGridSizerBody_Growables(self.flexGridSizerBody)
    self._init_coll_flexGridSizerBody_Items(self.flexGridSizerBody)

    self.SetSizer(self.boxSizerFrame)
    self.panelClient.SetSizer(self.flexGridSizerBody)
    self.panelBottom.SetSizer(self.boxSizerBottomPanel)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGSELX, name='DialogSelX', parent=prnt, pos=wx.Point(427, 187), size=wx.Size(440, 113),
      style=wx.DEFAULT_DIALOG_STYLE, title='Select Experiment')
    self.SetClientSize(wx.Size(424, 77))

    self.panelBottom = wx.Panel(id=wxID_DIALOGSELXPANELBOTTOM, name='panelBottom', parent=self, pos=wx.Point(0, 34), size=wx.Size(424, 43),
      style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGSELXBUTTONOK, label='&Ok', name='buttonOk', parent=self.panelBottom, pos=wx.Point(10, 10),
      size=wx.Size(192, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton, id=wxID_DIALOGSELXBUTTONOK)

    self.buttonCancel = wx.Button(id=wxID_DIALOGSELXBUTTONCANCEL, label='&Close', name='buttonCancel', parent=self.panelBottom, pos=wx.Point(222, 10),
      size=wx.Size(192, 23), style=0)
    self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton, id=wxID_DIALOGSELXBUTTONCANCEL)

    self.panelClient = wx.Panel(id=wxID_DIALOGSELXPANELCLIENT, name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(424, 34),
      style=wx.TAB_TRAVERSAL)

    self.staticTextExperiment = wx.StaticText(id=wxID_DIALOGSELXSTATICTEXTEXPERIMENT, label='Experiment', name='staticTextExperiment',
      parent=self.panelClient, pos=wx.Point(5, 9), size=wx.Size(55, 13), style=0)

    self.choiceExperiment = wx.Choice(choices=[], id=wxID_DIALOGSELXCHOICEEXPERIMENT, name='choiceExperiment', parent=self.panelClient,
      pos=wx.Point(75, 5), size=wx.Size(344, 21), style=0)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_choices()

  def init_choices(self):
    self.data = t_experiment.get_all_data(("id", "name"))
    for (id, name) in self.data:
      self.choiceExperiment.Append(name)


  def OnButtonOkButton(self, event):
    index = self.choiceExperiment.GetSelection()
    try:
      if index == wx.NOT_FOUND:
        raise error_x("Please select an experiment.")
        
      session.idexperiment = self.data[index][0]
        
        
    except error_x, e:
      output(e.message, OUTPUT_ERROR, True)


  def OnButtonCancelButton(self, event):
    self.Close()
