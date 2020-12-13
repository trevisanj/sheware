#Boa:Dialog:DialogEditTray

import wx
import act_main
from output import *
from errors import *
from table_tray import t_tray

def create(parent):
    return DialogEditTray(parent)

[wxID_DIALOGEDITTRAY, wxID_DIALOGEDITTRAYBUTTONCANCEL, wxID_DIALOGEDITTRAYBUTTONOK, wxID_DIALOGEDITTRAYPANELBOTTOM, 
 wxID_DIALOGEDITTRAYPANELCLIENT, wxID_DIALOGEDITTRAYSTATICTEXT1, wxID_DIALOGEDITTRAYSTATICTEXT2, 
 wxID_DIALOGEDITTRAYSTATICTEXT3, wxID_DIALOGEDITTRAYTEXTCTRLCOMMENTS, wxID_DIALOGEDITTRAYTEXTCTRLID, 
 wxID_DIALOGEDITTRAYTEXTCTRLNAME, 
] = [wx.NewId() for _init_ctrls in range(11)]

class DialogEditTray(wx.Dialog):
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
    wx.Dialog.__init__(self, id=wxID_DIALOGEDITTRAY, name='DialogEditTray', parent=prnt, pos=wx.Point(1648, 401), size=wx.Size(543, 222),
      style=wx.DEFAULT_DIALOG_STYLE, title='Tray')
    self.SetClientSize(wx.Size(527, 186))
    self.Center(wx.BOTH)

    self.panelBottom = wx.Panel(id=wxID_DIALOGEDITTRAYPANELBOTTOM, name='panelBottom', parent=self, pos=wx.Point(0, 143), size=wx.Size(527, 43),
      style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGEDITTRAYBUTTONOK, label='&Ok', name='buttonOk', parent=self.panelBottom, pos=wx.Point(10, 10),
      size=wx.Size(243, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton, id=wxID_DIALOGEDITTRAYBUTTONOK)

    self.buttonCancel = wx.Button(id=wxID_DIALOGEDITTRAYBUTTONCANCEL, label='&Cancel', name='buttonCancel', parent=self.panelBottom,
      pos=wx.Point(273, 10), size=wx.Size(243, 23), style=0)
    self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton, id=wxID_DIALOGEDITTRAYBUTTONCANCEL)

    self.panelClient = wx.Panel(id=wxID_DIALOGEDITTRAYPANELCLIENT, name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(527, 143),
      style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGEDITTRAYSTATICTEXT1, label='Id', name='staticText1', parent=self.panelClient, pos=wx.Point(5,
      9), size=wx.Size(11, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGEDITTRAYSTATICTEXT2, label='Name', name='staticText2', parent=self.panelClient,
      pos=wx.Point(5, 40), size=wx.Size(55, 13), style=0)

    self.staticText3 = wx.StaticText(id=wxID_DIALOGEDITTRAYSTATICTEXT3, label='Comments', name='staticText3', parent=self.panelClient,
      pos=wx.Point(5, 95), size=wx.Size(55, 13), style=0)

    self.textCtrlId = wx.TextCtrl(id=wxID_DIALOGEDITTRAYTEXTCTRLID, name='textCtrlId', parent=self.panelClient, pos=wx.Point(70, 5),
      size=wx.Size(100, 21), style=0, value='')
    self.textCtrlId.Enable(False)

    self.textCtrlName = wx.TextCtrl(id=wxID_DIALOGEDITTRAYTEXTCTRLNAME, name='textCtrlName', parent=self.panelClient, pos=wx.Point(70, 36),
      size=wx.Size(452, 21), style=0, value='')

    self.textCtrlComments = wx.TextCtrl(id=wxID_DIALOGEDITTRAYTEXTCTRLCOMMENTS, name='textCtrlComments', parent=self.panelClient,
      pos=wx.Point(70, 67), size=wx.Size(452, 70), style=wx.TE_MULTILINE, value='')

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.result = wx.ID_CANCEL

  def set_mode(self, mode):
    if mode == "insert":
      self.SetTitle("Insert tray")
    elif mode == "edit":
      self.SetTitle("Edit tray")
    else:
      raise error_x("Invalid mode: %s." % mode)
    self.mode = mode
    
    
  def set_id(self, value):
    self.textCtrlId.SetValue(str(value))

    row = t_tray.get_values_from_id(("id", "code", "comments"), value)
    self.set_code(row[1])
    self.set_comments(row[2])
  def get_id(self):
    return self.textCtrlId.GetValue()

    
  def set_code(self, value):
    self.textCtrlName.SetValue(str(value))
  def get_code(self):
    return self.textCtrlName.GetValue()
    
  def set_comments(self, value):
    self.textCtrlComments.SetValue(str(value))     
  def get_comments(self):
    return self.textCtrlComments.GetValue()
    
    

  def OnButtonOkButton(self, event):
    try:
      #Consistency
      
      code = self.get_code()
      if len(code) == 0:
        raise error_x("Please inform code.")
      comments = self.get_comments()
      
      if self.mode == "edit":
        d = {"code": code, "comments": comments}
        t_tray.update(d, self.get_id())
      else:
        d = {"code": code, "comments": comments, "idexperiment": self.idexperiment}
        t_tray.insert(d)

      self.result = wx.ID_OK
      self.Close()
    except error_x, e:
      output(e.message, OUTPUT_ERROR, True)
  

  def OnButtonCancelButton(self, event):
      self.Close()
