#Boa:Dialog:DialogEditClassifier

import wx
import act_main
import table_score
from output import *

def create(parent):
    return DialogEditClassifier(parent)

[wxID_DIALOGEDITCLASSIFIER, wxID_DIALOGEDITCLASSIFIERBUTTONCANCEL, wxID_DIALOGEDITCLASSIFIERBUTTONOK, wxID_DIALOGEDITCLASSIFIERCHOICE1, 
 wxID_DIALOGEDITCLASSIFIERCHOICESCOREGROUP, wxID_DIALOGEDITCLASSIFIERPANELBOTTOM, wxID_DIALOGEDITCLASSIFIERPANELCLIENT, 
 wxID_DIALOGEDITCLASSIFIERSTATICTEXT1, wxID_DIALOGEDITCLASSIFIERSTATICTEXT2, wxID_DIALOGEDITCLASSIFIERSTATICTEXT3, 
 wxID_DIALOGEDITCLASSIFIERSTATICTEXT4, wxID_DIALOGEDITCLASSIFIERSTATICTEXT5, wxID_DIALOGEDITCLASSIFIERTEXTCTRLID, 
 wxID_DIALOGEDITCLASSIFIERTEXTCTRLNAME, wxID_DIALOGEDITCLASSIFIERTEXTCTRLSCORES, 
] = [wx.NewId() for _init_ctrls in range(15)]

class DialogEditClassifier(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlId, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText2, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlName, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText3, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.choice1, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText5, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.choiceScoregroup, 0, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.staticText4, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlScores, 0, border=5, flag=wx.ALL | wx.GROW)

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

    self.flexGridSizer1 = wx.FlexGridSizer(cols=2, hgap=0, rows=4, vgap=0)

    self._init_coll_boxSizerFrame_Items(self.boxSizerFrame)
    self._init_coll_boxSizerBottomPanel_Items(self.boxSizerBottomPanel)
    self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
    self._init_coll_flexGridSizer1_Growables(self.flexGridSizer1)

    self.SetSizer(self.boxSizerFrame)
    self.panelClient.SetSizer(self.flexGridSizer1)
    self.panelBottom.SetSizer(self.boxSizerBottomPanel)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGEDITCLASSIFIER, name='DialogEditClassifier', parent=prnt, pos=wx.Point(447, 117), size=wx.Size(543, 290),
      style=wx.DEFAULT_DIALOG_STYLE, title='Classifier')
    self.SetClientSize(wx.Size(527, 254))
    self.Center(wx.BOTH)

    self.panelBottom = wx.Panel(id=wxID_DIALOGEDITCLASSIFIERPANELBOTTOM, name='panelBottom', parent=self, pos=wx.Point(0, 211), size=wx.Size(527, 43),
      style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGEDITCLASSIFIERBUTTONOK, label='&Ok', name='buttonOk', parent=self.panelBottom, pos=wx.Point(10, 10),
      size=wx.Size(243, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton, id=wxID_DIALOGEDITCLASSIFIERBUTTONOK)

    self.buttonCancel = wx.Button(id=wxID_DIALOGEDITCLASSIFIERBUTTONCANCEL, label='&Cancel', name='buttonCancel', parent=self.panelBottom,
      pos=wx.Point(273, 10), size=wx.Size(243, 23), style=0)
    self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton, id=wxID_DIALOGEDITCLASSIFIERBUTTONCANCEL)

    self.panelClient = wx.Panel(id=wxID_DIALOGEDITCLASSIFIERPANELCLIENT, name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(527, 211),
      style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGEDITCLASSIFIERSTATICTEXT1, label='Id', name='staticText1', parent=self.panelClient, pos=wx.Point(5,
      9), size=wx.Size(11, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGEDITCLASSIFIERSTATICTEXT2, label='Name', name='staticText2', parent=self.panelClient,
      pos=wx.Point(5, 40), size=wx.Size(55, 13), style=0)

    self.staticText3 = wx.StaticText(id=wxID_DIALOGEDITCLASSIFIERSTATICTEXT3, label='Internal class', name='staticText3', parent=self.panelClient,
      pos=wx.Point(5, 71), size=wx.Size(75, 13), style=0)

    self.staticText4 = wx.StaticText(id=wxID_DIALOGEDITCLASSIFIERSTATICTEXT4, label='Parameters', name='staticText4', parent=self.panelClient,
      pos=wx.Point(5, 159), size=wx.Size(55, 13), style=0)

    self.textCtrlId = wx.TextCtrl(id=wxID_DIALOGEDITCLASSIFIERTEXTCTRLID, name='textCtrlId', parent=self.panelClient, pos=wx.Point(90, 5),
      size=wx.Size(54, 21), style=0, value='')
    self.textCtrlId.Enable(False)

    self.textCtrlName = wx.TextCtrl(id=wxID_DIALOGEDITCLASSIFIERTEXTCTRLNAME, name='textCtrlName', parent=self.panelClient, pos=wx.Point(90, 36),
      size=wx.Size(432, 21), style=0, value='')

    self.textCtrlScores = wx.TextCtrl(id=wxID_DIALOGEDITCLASSIFIERTEXTCTRLSCORES, name='textCtrlScores', parent=self.panelClient, pos=wx.Point(90,
      129), size=wx.Size(432, 73), style=wx.TE_MULTILINE, value='')

    self.choice1 = wx.Choice(choices=[], id=wxID_DIALOGEDITCLASSIFIERCHOICE1, name='choice1', parent=self.panelClient, pos=wx.Point(90, 67),
      size=wx.Size(432, 21), style=0)

    self.staticText5 = wx.StaticText(id=wxID_DIALOGEDITCLASSIFIERSTATICTEXT5, label='Score group', name='staticText5', parent=self.panelClient,
      pos=wx.Point(5, 102), size=wx.Size(55, 13), style=0)

    self.choiceScoregroup = wx.Choice(choices=[], id=wxID_DIALOGEDITCLASSIFIERCHOICESCOREGROUP, name='choiceScoregroup', parent=self.panelClient,
      pos=wx.Point(90, 98), size=wx.Size(432, 21), style=0)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)

  def set_mode(self, mode):
    if mode == "insert":
      self.SetTitle("Insert score group")
    elif mode == "edit":
      self.SetTitle("Edit score group")
    else:
      raise error_x("Invalid mode: %s." % mode)
    
    
  def set_id(self, value):
    self.textCtrlId.SetValue(str(value))
    
  def set_name(self, value):
    self.textCtrlName.SetValue(str(value))
    
  def set_comments(self, value):
    self.textCtrlComments.SetValue(str(value))     
    
  def set_scores(self, value):
    self.textCtrlScores.SetValue(str(value))
    

  def OnButtonOkButton(self, event):
    try:
      #Consistency
      
      name = self.textCtrlName.GetValue()
      if len(name) == 0:
        raise error_x("Please inform name.")
      scores = table_score.sanitize(self.textCtrlScores.GetValue())
      
      self.name = name
      self.comments = self.textCtrlComments.GetValue()
      self.scores = scores
        
      self.result = wx.ID_OK
      self.Close()
        
    except error_x, e:
      output(e.message, OUTPUT_ERROR, True)

  def OnButtonCancelButton(self, event):
      self.result = wx.ID_CANCEL
      self.Close()
