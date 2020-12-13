#Boa:Dialog:DialogRunTrain

import wx
import act_main, act_run_train
from table_judge import t_judge
from output import *
from errors import *

def create(parent):
    return DialogRunTrain(parent)

[wxID_DIALOGRUNTRAIN, wxID_DIALOGRUNTRAINBUTTONOK, wxID_DIALOGRUNTRAINBUTTONRUN, wxID_DIALOGRUNTRAINBUTTONTRAIN, wxID_DIALOGRUNTRAINCHOICEREFERENCE, 
 wxID_DIALOGRUNTRAINCHOICEUSE, wxID_DIALOGRUNTRAINPANELBOTTOM, wxID_DIALOGRUNTRAINPANELCLIENT, wxID_DIALOGRUNTRAINSTATICTEXT1, 
 wxID_DIALOGRUNTRAINSTATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(10)]

class DialogRunTrain(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.choiceUse, 0, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.buttonRun, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText2, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.choiceReference, 0, border=5, flag=wx.EXPAND | wx.ALL)
    parent.AddWindow(self.buttonTrain, 0, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizerBottomPanel_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonOk, 1, border=10, flag=wx.ALL | wx.ALIGN_RIGHT)

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

    self.flexGridSizer1 = wx.FlexGridSizer(cols=3, hgap=0, rows=4, vgap=0)

    self._init_coll_boxSizerFrame_Items(self.boxSizerFrame)
    self._init_coll_boxSizerBottomPanel_Items(self.boxSizerBottomPanel)
    self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
    self._init_coll_flexGridSizer1_Growables(self.flexGridSizer1)

    self.SetSizer(self.boxSizerFrame)
    self.panelClient.SetSizer(self.flexGridSizer1)
    self.panelBottom.SetSizer(self.boxSizerBottomPanel)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGRUNTRAIN, name='DialogRunTrain', parent=prnt, pos=wx.Point(1648, 340), size=wx.Size(543, 152),
      style=wx.DEFAULT_DIALOG_STYLE, title='Classifier running and training')
    self.SetClientSize(wx.Size(527, 116))
    self.Center(wx.BOTH)

    self.panelBottom = wx.Panel(id=wxID_DIALOGRUNTRAINPANELBOTTOM, name='panelBottom', parent=self, pos=wx.Point(0, 73), size=wx.Size(527, 43),
      style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGRUNTRAINBUTTONOK, label='&Close', name='buttonOk', parent=self.panelBottom, pos=wx.Point(10, 10),
      size=wx.Size(507, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton, id=wxID_DIALOGRUNTRAINBUTTONOK)

    self.panelClient = wx.Panel(id=wxID_DIALOGRUNTRAINPANELCLIENT, name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(527, 73),
      style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGRUNTRAINSTATICTEXT1, label='Classifier to run/train', name='staticText1', parent=self.panelClient,
      pos=wx.Point(5, 12), size=wx.Size(107, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGRUNTRAINSTATICTEXT2, label='Reference judge', name='staticText2', parent=self.panelClient,
      pos=wx.Point(5, 48), size=wx.Size(107, 13), style=0)

    self.choiceUse = wx.Choice(choices=[], id=wxID_DIALOGRUNTRAINCHOICEUSE, name='choiceUse', parent=self.panelClient, pos=wx.Point(122, 5),
      size=wx.Size(315, 21), style=0)

    self.buttonRun = wx.Button(id=wxID_DIALOGRUNTRAINBUTTONRUN, label='&Run', name='buttonRun', parent=self.panelClient, pos=wx.Point(447, 5),
      size=wx.Size(75, 27), style=0)
    self.buttonRun.Bind(wx.EVT_BUTTON, self.OnButtonRunButton, id=wxID_DIALOGRUNTRAINBUTTONRUN)

    self.choiceReference = wx.Choice(choices=[], id=wxID_DIALOGRUNTRAINCHOICEREFERENCE, name='choiceReference', parent=self.panelClient,
      pos=wx.Point(122, 42), size=wx.Size(315, 21), style=0)

    self.buttonTrain = wx.Button(id=wxID_DIALOGRUNTRAINBUTTONTRAIN, label='&Train', name='buttonTrain', parent=self.panelClient, pos=wx.Point(447,
      42), size=wx.Size(75, 26), style=0)
    self.buttonTrain.Bind(wx.EVT_BUTTON, self.OnButtonTrainButton, id=wxID_DIALOGRUNTRAINBUTTONTRAIN)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_choices()

    
  def init_choices(self):
    self.data_cl = list(t_judge.get_all_data(("id", "name")))
    for (id, name) in self.data_cl:
      self.choiceUse.Append(name)
      self.choiceReference.Append(name)
    
    s = "<<< All >>>"
    self.choiceUse.Append(s)
    self.data_cl.append((-10000, s))

  def get_idjudge_use(self):
    index = self.choiceUse.GetSelection()
    if index < 0:
      raise error_x("No judge to run/train selected!")
    return self.data_cl[index][0]
  
  def get_idjudge_reference(self):
    index = self.choiceReference.GetSelection()
    if index < 0:
      raise error_x("No reference judge selected!")
    return self.data_cl[index][0]
  


  def OnButtonOkButton(self, event):
    try:
      self.result = wx.ID_OK
      self.Close()
        
    except error_x, e:
      output(e.message, OUTPUT_ERROR, True)

  def OnButtonRunButton(self, event):
    try:
      act_run_train.run(self.get_idjudge_use())
    except error_x, e:
      act_main.handle_error(e)
      

  def OnButtonTrainButton(self, event):
    try:
      act_run_train.train(self.get_idjudge_use(), self.get_idjudge_reference())
    except error_x, e:
      act_main.handle_error(e)

