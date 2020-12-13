#Boa:Dialog:DialogEditScoregroup

import wx
import act_main
import table_score
from output import *
from errors import *
from table_score import t_score
from table_scoregroup import t_scoregroup

def create(parent):
    return DialogEditScoregroup(parent)

[wxID_DIALOGEDITSCOREGROUP, wxID_DIALOGEDITSCOREGROUPBUTTONCANCEL, wxID_DIALOGEDITSCOREGROUPBUTTONOK, wxID_DIALOGEDITSCOREGROUPPANELBOTTOM, 
 wxID_DIALOGEDITSCOREGROUPPANELCLIENT, wxID_DIALOGEDITSCOREGROUPSTATICTEXT1, wxID_DIALOGEDITSCOREGROUPSTATICTEXT2, 
 wxID_DIALOGEDITSCOREGROUPSTATICTEXT3, wxID_DIALOGEDITSCOREGROUPSTATICTEXT4, wxID_DIALOGEDITSCOREGROUPTEXTCTRLCOMMENTS, 
 wxID_DIALOGEDITSCOREGROUPTEXTCTRLID, wxID_DIALOGEDITSCOREGROUPTEXTCTRLNAME, wxID_DIALOGEDITSCOREGROUPTEXTCTRLSCORES, 
] = [wx.NewId() for _init_ctrls in range(13)]

class DialogEditScoregroup(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlId, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText2, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlName, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText3, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.textCtrlComments, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText4, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlScores, 0, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizerBottomPanel_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonOk, 1, border=10, flag=wx.ALIGN_RIGHT)
    parent.AddWindow(self.buttonCancel, 1, border=10, flag=wx.ALIGN_RIGHT)

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
    self.panelBottom.SetSizer(self.boxSizerBottomPanel)
    self.panelClient.SetSizer(self.flexGridSizer1)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGEDITSCOREGROUP, name='DialogEditScoregroup', parent=prnt, pos=wx.Point(318, 256), size=wx.Size(543, 287),
      style=wx.DEFAULT_DIALOG_STYLE, title='Score group')
    self.SetClientSize(wx.Size(527, 251))
    self.Center(wx.BOTH)

    self.panelBottom = wx.Panel(id=wxID_DIALOGEDITSCOREGROUPPANELBOTTOM, name='panelBottom', parent=self, pos=wx.Point(0, 228), size=wx.Size(527, 23),
      style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGEDITSCOREGROUPBUTTONOK, label='&Ok', name='buttonOk', parent=self.panelBottom, pos=wx.Point(0, 0),
      size=wx.Size(263, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton, id=wxID_DIALOGEDITSCOREGROUPBUTTONOK)

    self.buttonCancel = wx.Button(id=wxID_DIALOGEDITSCOREGROUPBUTTONCANCEL, label='&Cancel', name='buttonCancel', parent=self.panelBottom,
      pos=wx.Point(263, 0), size=wx.Size(263, 23), style=0)
    self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton, id=wxID_DIALOGEDITSCOREGROUPBUTTONCANCEL)

    self.panelClient = wx.Panel(id=wxID_DIALOGEDITSCOREGROUPPANELCLIENT, name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(527, 228),
      style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGEDITSCOREGROUPSTATICTEXT1, label='Id', name='staticText1', parent=self.panelClient, pos=wx.Point(5,
      9), size=wx.Size(11, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGEDITSCOREGROUPSTATICTEXT2, label='Name', name='staticText2', parent=self.panelClient,
      pos=wx.Point(5, 40), size=wx.Size(55, 13), style=0)

    self.staticText3 = wx.StaticText(id=wxID_DIALOGEDITSCOREGROUPSTATICTEXT3, label='Comments', name='staticText3', parent=self.panelClient,
      pos=wx.Point(5, 95), size=wx.Size(55, 13), style=0)

    self.staticText4 = wx.StaticText(id=wxID_DIALOGEDITSCOREGROUPSTATICTEXT4, label='Scores', name='staticText4', parent=self.panelClient,
      pos=wx.Point(5, 177), size=wx.Size(55, 13), style=0)

    self.textCtrlId = wx.TextCtrl(id=wxID_DIALOGEDITSCOREGROUPTEXTCTRLID, name='textCtrlId', parent=self.panelClient, pos=wx.Point(70, 5),
      size=wx.Size(100, 21), style=0, value='')
    self.textCtrlId.Enable(False)

    self.textCtrlName = wx.TextCtrl(id=wxID_DIALOGEDITSCOREGROUPTEXTCTRLNAME, name='textCtrlName', parent=self.panelClient, pos=wx.Point(70, 36),
      size=wx.Size(452, 21), style=0, value='')

    self.textCtrlComments = wx.TextCtrl(id=wxID_DIALOGEDITSCOREGROUPTEXTCTRLCOMMENTS, name='textCtrlComments', parent=self.panelClient,
      pos=wx.Point(70, 67), size=wx.Size(452, 70), style=wx.TE_MULTILINE, value='')

    self.textCtrlScores = wx.TextCtrl(id=wxID_DIALOGEDITSCOREGROUPTEXTCTRLSCORES, name='textCtrlScores', parent=self.panelClient, pos=wx.Point(70,
      147), size=wx.Size(452, 73), style=wx.TE_MULTILINE, value='')

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.result = wx.ID_CANCEL

  def set_mode(self, mode):
    if mode == "insert":
      self.SetTitle("Insert score group")
    elif mode == "edit":
      self.SetTitle("Edit score group")
    else:
      raise error_x("Invalid mode: %s." % mode)
    self.mode = mode
    
    
  def set_id(self, value):
    self.textCtrlId.SetValue(str(value))

    row = t_scoregroup.get_values_from_id(("id", "name", "comments"), value)
    self.set_name(row[1])
    self.set_comments(row[2])
    self.set_scores(t_score.get_string_1scoregroup(value))
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
    
  def set_scores(self, value):
    self.textCtrlScores.SetValue(str(value))
  def get_scores(self):
    return self.textCtrlScores.GetValue()
    

  def OnButtonOkButton(self, event):
    try:
      #Consistency
      
      name = self.get_name()
      if len(name) == 0:
        raise error_x("Please inform name.")
      scores = table_score.sanitize(self.get_scores())
      comments = self.get_comments()
      d = {"name": name, "comments": comments, "scores": scores}
      
      if self.mode == "edit":
        t_scoregroup.update(d, self.get_id())
      else:
        t_scoregroup.insert(d)

      self.result = wx.ID_OK
      self.Close()
    except error_x, e:
      act_main.handle_exception(e)
  

  def OnButtonCancelButton(self, event):
      self.Close()
