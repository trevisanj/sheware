#Boa:Dialog:DialogEditDomain

import wx
import act_main
from table_domain import t_domain
from table_scoregroup import t_scoregroup
from output import *
import act_domain
from errors import *

def create(parent):
    return DialogEditDomain(parent)

[wxID_DIALOGEDITDOMAIN, wxID_DIALOGEDITDOMAINBUTTONCANCEL, 
 wxID_DIALOGEDITDOMAINBUTTONOK, wxID_DIALOGEDITDOMAINPANELBOTTOM, 
 wxID_DIALOGEDITDOMAINPANELCLIENT, wxID_DIALOGEDITDOMAINSTATICTEXT1, 
 wxID_DIALOGEDITDOMAINSTATICTEXT2, wxID_DIALOGEDITDOMAINSTATICTEXT3, 
 wxID_DIALOGEDITDOMAINSTATICTEXT4, wxID_DIALOGEDITDOMAINSTATICTEXTCOMMENTS, 
 wxID_DIALOGEDITDOMAINSTATICTEXTWNCOUNT, 
 wxID_DIALOGEDITDOMAINTEXTCTRLCOMMENTS, wxID_DIALOGEDITDOMAINTEXTCTRLID, 
 wxID_DIALOGEDITDOMAINTEXTCTRLNAME, wxID_DIALOGEDITDOMAINTEXTCTRLWNCOUNT, 
 wxID_DIALOGEDITDOMAINTEXTCTRL_WN1, wxID_DIALOGEDITDOMAINTEXTCTRL_WN2, 
] = [wx.NewId() for _init_ctrls in range(17)]

class DialogEditDomain(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=5,
          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlId, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText2, 0, border=5,
          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlName, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticTextWncount, 0, border=5,
          flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.textCtrlWncount, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText3, 0, border=5,
          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrl_wn1, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText4, 0, border=5,
          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrl_wn2, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticTextComments, 0, border=5,
          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlComments, 0, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizerBottomPanel_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonOk, 1, border=10, flag=wx.ALL | wx.ALIGN_RIGHT)
    parent.AddWindow(self.buttonCancel, 1, border=10,
          flag=wx.ALL | wx.ALIGN_RIGHT)

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

    self.flexGridSizer1 = wx.FlexGridSizer(cols=2, hgap=0, rows=5, vgap=0)

    self._init_coll_boxSizerFrame_Items(self.boxSizerFrame)
    self._init_coll_boxSizerBottomPanel_Items(self.boxSizerBottomPanel)
    self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
    self._init_coll_flexGridSizer1_Growables(self.flexGridSizer1)

    self.SetSizer(self.boxSizerFrame)
    self.panelBottom.SetSizer(self.boxSizerBottomPanel)
    self.panelClient.SetSizer(self.flexGridSizer1)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGEDITDOMAIN, name='DialogEditDomain',
          parent=prnt, pos=wx.Point(518, 394), size=wx.Size(555, 281),
          style=wx.DEFAULT_DIALOG_STYLE, title='Domain')
    self.SetClientSize(wx.Size(555, 281))
    self.Center(wx.BOTH)

    self.panelBottom = wx.Panel(id=wxID_DIALOGEDITDOMAINPANELBOTTOM,
          name='panelBottom', parent=self, pos=wx.Point(0, 238),
          size=wx.Size(555, 43), style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGEDITDOMAINBUTTONOK, label='&Ok',
          name='buttonOk', parent=self.panelBottom, pos=wx.Point(10, 10),
          size=wx.Size(257, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton,
          id=wxID_DIALOGEDITDOMAINBUTTONOK)

    self.buttonCancel = wx.Button(id=wxID_DIALOGEDITDOMAINBUTTONCANCEL,
          label='&Cancel', name='buttonCancel', parent=self.panelBottom,
          pos=wx.Point(287, 10), size=wx.Size(257, 23), style=0)
    self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton,
          id=wxID_DIALOGEDITDOMAINBUTTONCANCEL)

    self.panelClient = wx.Panel(id=wxID_DIALOGEDITDOMAINPANELCLIENT,
          name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(555,
          238), style=wx.TAB_TRAVERSAL)
    self.panelClient.SetAutoLayout(False)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGEDITDOMAINSTATICTEXT1,
          label='Id', name='staticText1', parent=self.panelClient,
          pos=wx.Point(5, 9), size=wx.Size(11, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGEDITDOMAINSTATICTEXT2,
          label='Name', name='staticText2', parent=self.panelClient,
          pos=wx.Point(5, 40), size=wx.Size(55, 13), style=0)

    self.staticTextWncount = wx.StaticText(id=wxID_DIALOGEDITDOMAINSTATICTEXTWNCOUNT,
          label='Wncount', name='staticTextWncount', parent=self.panelClient,
          pos=wx.Point(5, 71), size=wx.Size(75, 13), style=0)

    self.staticTextComments = wx.StaticText(id=wxID_DIALOGEDITDOMAINSTATICTEXTCOMMENTS,
          label='Comments', name='staticTextComments', parent=self.panelClient,
          pos=wx.Point(5, 196), size=wx.Size(55, 13), style=0)

    self.textCtrlId = wx.TextCtrl(id=wxID_DIALOGEDITDOMAINTEXTCTRLID,
          name='textCtrlId', parent=self.panelClient, pos=wx.Point(90, 5),
          size=wx.Size(54, 21), style=0, value='')
    self.textCtrlId.Enable(False)

    self.textCtrlName = wx.TextCtrl(id=wxID_DIALOGEDITDOMAINTEXTCTRLNAME,
          name='textCtrlName', parent=self.panelClient, pos=wx.Point(90, 36),
          size=wx.Size(460, 21), style=0, value='')

    self.textCtrlComments = wx.TextCtrl(id=wxID_DIALOGEDITDOMAINTEXTCTRLCOMMENTS,
          name='textCtrlComments', parent=self.panelClient, pos=wx.Point(90,
          172), size=wx.Size(460, 73), style=wx.TE_MULTILINE, value='')

    self.textCtrlWncount = wx.TextCtrl(id=wxID_DIALOGEDITDOMAINTEXTCTRLWNCOUNT,
          name='textCtrlWncount', parent=self.panelClient, pos=wx.Point(90, 67),
          size=wx.Size(460, 21), style=0, value='')

    self.staticText3 = wx.StaticText(id=wxID_DIALOGEDITDOMAINSTATICTEXT3,
          label=u'Wn initial', name='staticText3', parent=self.panelClient,
          pos=wx.Point(5, 103), size=wx.Size(62, 17), style=0)

    self.staticText4 = wx.StaticText(id=wxID_DIALOGEDITDOMAINSTATICTEXT4,
          label=u'Wn final', name='staticText4', parent=self.panelClient,
          pos=wx.Point(5, 140), size=wx.Size(53, 17), style=0)

    self.textCtrl_wn1 = wx.TextCtrl(id=wxID_DIALOGEDITDOMAINTEXTCTRL_WN1,
          name=u'textCtrl_wn1', parent=self.panelClient, pos=wx.Point(90, 98),
          size=wx.Size(80, 27), style=0, value=u'')

    self.textCtrl_wn2 = wx.TextCtrl(id=wxID_DIALOGEDITDOMAINTEXTCTRL_WN2,
          name=u'textCtrl_wn2', parent=self.panelClient, pos=wx.Point(90, 135),
          size=wx.Size(80, 27), style=0, value=u'')

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_choices()
    self.result = wx.ID_CANCEL

  def init_choices(self):
    pass
  
    # Model
    #self.data_scoregroup = t_scoregroup.get_all_data(("id", "name"))
    #for (id, name) in self.data_scoregroup:
    #  self.choiceScoregroup.Append(name)
      
  def set_mode(self, mode):
    if mode == "insert":
      self.SetTitle("Insert Domain")
    elif mode == "edit":
      self.SetTitle("Edit Domain")
    else:
      raise error_x("Invalid mode: %s." % mode)
    self.mode = mode
    
    
  def set_id(self, value):
    self.textCtrlId.SetValue(str(value))
    
    row = t_domain.get_values_from_id(("id", "name", "wncount", "wn1", "wn2", "comments"), value)
    self.set_name(row[1])
    self.set_wncount(row[2])
    self.set_wn1(row[3])
    self.set_wn2(row[4])
    self.set_comments(row[5])
  def get_id(self):
    return self.textCtrlId.GetValue()
    
  def set_name(self, value):
    self.textCtrlName.SetValue(str(value))
  def get_name(self):
    return self.textCtrlName.GetValue()
   
  def set_wncount(self, value):
    self.textCtrlWncount.SetValue(str(value))
  def get_wncount(self):
    return self.textCtrlWncount.GetValue()
  
  def set_wn1(self, value):
    self.textCtrl_wn1.SetValue(str(value))
  def get_wn1(self):
    return self.textCtrl_wn1.GetValue()

  def set_wn2(self, value):
    self.textCtrl_wn2.SetValue(str(value))
  def get_wn2(self):
    return self.textCtrl_wn2.GetValue()

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
      
      wn1 = self.get_wn1()
      wn2 = self.get_wn2()
      wncount = self.get_wncount()
      # I don't check wncount ... TODO ... mysql error if non-numerical shit
      comments = self.get_comments()
      
      d = {"name": name, "wn1": wn1, "wn2": wn2, "wncount": wncount, "comments": comments}      
      if self.mode == "edit":
        t_domain.update(d, self.get_id())
      else:
        t_domain.insert(d)

      self.result = wx.ID_OK
      self.Close()
    except error_x, e:
      output(e.message, OUTPUT_ERROR, True)
  

  def OnButtonCancelButton(self, event):
      self.Close()
