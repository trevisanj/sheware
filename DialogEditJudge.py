#Boa:Dialog:DialogEditJudge

import wx
import act_main
from table_judge import t_judge
from table_scoregroup import t_scoregroup
from output import *
import act_judge
from errors import *

def create(parent):
    return DialogEditJudge(parent)

[wxID_DIALOGEDITJUDGE, wxID_DIALOGEDITJUDGEBUTTONCANCEL, wxID_DIALOGEDITJUDGEBUTTONOK, wxID_DIALOGEDITJUDGECHOICE1, 
 wxID_DIALOGEDITJUDGECHOICESCOREGROUP, wxID_DIALOGEDITJUDGEPANELBOTTOM, wxID_DIALOGEDITJUDGEPANELCLIENT, wxID_DIALOGEDITJUDGESTATICTEXT1, 
 wxID_DIALOGEDITJUDGESTATICTEXT2, wxID_DIALOGEDITJUDGESTATICTEXT3, wxID_DIALOGEDITJUDGESTATICTEXT4, wxID_DIALOGEDITJUDGESTATICTEXT5, 
 wxID_DIALOGEDITJUDGETEXTCTRLID, wxID_DIALOGEDITJUDGETEXTCTRLNAME, wxID_DIALOGEDITJUDGETEXTCTRLPARAMS, wxID_DIALOGEDITJUDGECHOICECLASS_NAME
] = [wx.NewId() for _init_ctrls in range(16)]

class DialogEditJudge(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlId, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.staticText2, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlName, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText3, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.choiceClass_name, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticText5, 0, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
    parent.AddWindow(self.choiceScoregroup, 0, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.staticText4, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.textCtrlParams, 0, border=5, flag=wx.ALL | wx.GROW)

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
    self.panelBottom.SetSizer(self.boxSizerBottomPanel)
    self.panelClient.SetSizer(self.flexGridSizer1)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGEDITJUDGE, name='DialogEditJudge', parent=prnt, pos=wx.Point(1652, 371), size=wx.Size(535, 281),
      style=wx.DEFAULT_DIALOG_STYLE, title='Classifier')
    self.SetClientSize(wx.Size(527, 254))
    self.Center(wx.BOTH)

    self.panelBottom = wx.Panel(id=wxID_DIALOGEDITJUDGEPANELBOTTOM, name='panelBottom', parent=self, pos=wx.Point(0, 211), size=wx.Size(527, 43),
      style=wx.TAB_TRAVERSAL)

    self.buttonOk = wx.Button(id=wxID_DIALOGEDITJUDGEBUTTONOK, label='&Ok', name='buttonOk', parent=self.panelBottom, pos=wx.Point(10, 10),
      size=wx.Size(243, 23), style=0)
    self.buttonOk.SetDefault()
    self.buttonOk.Bind(wx.EVT_BUTTON, self.OnButtonOkButton, id=wxID_DIALOGEDITJUDGEBUTTONOK)

    self.buttonCancel = wx.Button(id=wxID_DIALOGEDITJUDGEBUTTONCANCEL, label='&Cancel', name='buttonCancel', parent=self.panelBottom,
      pos=wx.Point(273, 10), size=wx.Size(243, 23), style=0)
    self.buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancelButton, id=wxID_DIALOGEDITJUDGEBUTTONCANCEL)

    self.panelClient = wx.Panel(id=wxID_DIALOGEDITJUDGEPANELCLIENT, name='panelClient', parent=self, pos=wx.Point(0, 0), size=wx.Size(527, 211),
      style=wx.TAB_TRAVERSAL)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGEDITJUDGESTATICTEXT1, label='Id', name='staticText1', parent=self.panelClient, pos=wx.Point(5, 9),
      size=wx.Size(11, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGEDITJUDGESTATICTEXT2, label='Name', name='staticText2', parent=self.panelClient, pos=wx.Point(5,
      40), size=wx.Size(55, 13), style=0)

    self.staticText3 = wx.StaticText(id=wxID_DIALOGEDITJUDGESTATICTEXT3, label='Internal class', name='staticText3', parent=self.panelClient,
      pos=wx.Point(5, 71), size=wx.Size(75, 13), style=0)

    self.staticText4 = wx.StaticText(id=wxID_DIALOGEDITJUDGESTATICTEXT4, label='Parameters', name='staticText4', parent=self.panelClient,
      pos=wx.Point(5, 159), size=wx.Size(55, 13), style=0)

    self.textCtrlId = wx.TextCtrl(id=wxID_DIALOGEDITJUDGETEXTCTRLID, name='textCtrlId', parent=self.panelClient, pos=wx.Point(90, 5), size=wx.Size(54,
      21), style=0, value='')
    self.textCtrlId.Enable(False)

    self.textCtrlName = wx.TextCtrl(id=wxID_DIALOGEDITJUDGETEXTCTRLNAME, name='textCtrlName', parent=self.panelClient, pos=wx.Point(90, 36),
      size=wx.Size(432, 21), style=0, value='')

    self.textCtrlParams = wx.TextCtrl(id=wxID_DIALOGEDITJUDGETEXTCTRLPARAMS, name='textCtrlParams', parent=self.panelClient, pos=wx.Point(90, 129),
      size=wx.Size(432, 73), style=wx.TE_MULTILINE, value='')

    self.choiceClass_name = wx.Choice(choices=[], id=wxID_DIALOGEDITJUDGECHOICECLASS_NAME, name='choiceClass_name', parent=self.panelClient,
      pos=wx.Point(90, 67), size=wx.Size(432, 21), style=0)

    self.staticText5 = wx.StaticText(id=wxID_DIALOGEDITJUDGESTATICTEXT5, label='Score group', name='staticText5', parent=self.panelClient,
      pos=wx.Point(5, 102), size=wx.Size(75, 13), style=0)

    self.choiceScoregroup = wx.Choice(choices=[], id=wxID_DIALOGEDITJUDGECHOICESCOREGROUP, name='choiceScoregroup', parent=self.panelClient,
      pos=wx.Point(90, 98), size=wx.Size(432, 21), style=0)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_choices()
    self.result = wx.ID_CANCEL

  def init_choices(self):
    self.data_scoregroup = t_scoregroup.get_all_data(("id", "name"))
    for (id, name) in self.data_scoregroup:
      self.choiceScoregroup.Append(name)
      
    #self.class_names = ["judge_data_density", "judge_diff2_energy", "judge_diff2_var", "judge_diff_energy", "judge_diff_var", "judge_distance", "judge_score_human", "judge_trend_shift"]
    #self.class_names.sort();
    self.data_judge_classes = act_judge.get_judge_classes()
    for (cl, desc, flag_score) in self.data_judge_classes:
      self.choiceClass_name.Append(desc)

  def set_mode(self, mode):
    if mode == "insert":
      self.SetTitle("Insert Classifier")
    elif mode == "edit":
      self.SetTitle("Edit Classifier")
    else:
      raise error_x("Invalid mode: %s." % mode)
    self.mode = mode
    
    
  def set_id(self, value):
    self.textCtrlId.SetValue(str(value))
    
    row = t_judge.get_values_from_id(("id", "name", "class_name", "params", "idscoregroup"), value)
    self.set_name(row[1])
    self.set_class_name(row[2])
    self.set_params(row[3])
    self.set_idscoregroup(row[4])
  def get_id(self):
    return self.textCtrlId.GetValue()
    
  def set_name(self, value):
    self.textCtrlName.SetValue(str(value))
  def get_name(self):
    return self.textCtrlName.GetValue()
    
  def set_class_name(self, value):
    i = 0
    idx = -1
    for row in self.data_judge_classes:
      if value == row[0]:
        idx = i
        break
      i += 1
    self.choiceClass_name.SetSelection(idx)
  def get_class_name(self):
    idx = self.choiceClass_name.GetSelection()
    if idx == -1:
      return ''
    else:
      return self.data_judge_classes[idx][0]
  def get_class_index(self):
    return self.choiceClass_name.GetSelection()
  
  def set_idscoregroup(self, value):
    i = 0
    idx = -1
    for row in self.data_scoregroup:
      if value == row[0]:
        idx = i
        break
      i += 1
    self.choiceScoregroup.SetSelection(idx)
  def get_idscoregroup(self):
    idx = self.choiceScoregroup.GetSelection()
    if idx == -1:
      return 0
    else:
      return self.data_scoregroup[idx][0]
  
  def set_params(self, value):
    self.textCtrlParams.SetValue(str(value))
  def get_params(self):
    return self.textCtrlParams.GetValue()
        

  def OnButtonOkButton(self, event):
    try:
      #Consistency
      
      name = self.get_name()
      if len(name) == 0:
        raise error_x("Please inform name.")
      
      class_idx = self.get_class_index()
      if class_idx == -1:
        raise error_x("Please inform class name.")
      class_name = self.data_judge_classes[class_idx][0]
      flag_score = self.data_judge_classes[class_idx][2]
      
      idscoregroup = self.get_idscoregroup()
      if flag_score and idscoregroup < 1:
        raise error_x("Score group is required for class '%s'!" % class_name)
      
      params = self.get_params()
      
      d = {"name": name, "class_name": class_name, "idscoregroup": idscoregroup, "params": params}      
      if self.mode == "edit":
        t_judge.update(d, self.get_id())
      else:
        t_judge.insert(d)

      self.result = wx.ID_OK
      self.Close()
    except error_x, e:
      output(e.message, OUTPUT_ERROR, True)
  

  def OnButtonCancelButton(self, event):
      self.Close()
