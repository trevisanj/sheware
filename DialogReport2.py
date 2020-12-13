#Boa:Dialog:DialogReport1
import wx, wx.grid, db_con, session, act_report2

from table_colony import t_colony
from table_judge import t_judge
from table_score import t_score
from table_colony_judge import t_colony_judge
from output import *

def create(parent):
    return DialogReport1(parent)

[wxID_DIALOGREPORT1, wxID_DIALOGREPORT1BUTTONGENERATE, wxID_DIALOGREPORT1CHECKLISTBOXCLASSIFIERS, wxID_DIALOGREPORT1CHOICECLASSIFIER, 
 wxID_DIALOGREPORT1PANEL1, wxID_DIALOGREPORT1STATICTEXTCLASSIFIER, wxID_DIALOGREPORT1STATICTEXTREFERENCECLASSIFIER, 
] = [wx.NewId() for _init_ctrls in range(7)]

class DialogReport1(wx.Dialog):
  def _init_coll_flexGridSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticTextReferenceClassifier, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.choiceClassifier, 0, border=5, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.staticTextClassifier, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.checkListBoxClassifiers, 0, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizerBody_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panel1, 1, border=0, flag=wx.GROW)
    parent.AddWindow(self.buttonGenerate, 0, border=10, flag=wx.ALL)

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
    wx.Dialog.__init__(self, id=wxID_DIALOGREPORT1, name='DialogReport1', parent=prnt, pos=wx.Point(346, 430), size=wx.Size(602, 244),
      style=wx.DEFAULT_FRAME_STYLE, title='Scan scores report')
    self.SetClientSize(wx.Size(586, 208))
    self.SetToolTipString('DialogTray')

    self.panel1 = wx.Panel(id=wxID_DIALOGREPORT1PANEL1, name='panel1', parent=self, pos=wx.Point(0, 0), size=wx.Size(491, 208),
      style=wx.TAB_TRAVERSAL)
    self.panel1.SetMinSize(wx.Size(534, 83))

    self.staticTextClassifier = wx.StaticText(id=wxID_DIALOGREPORT1STATICTEXTCLASSIFIER, label='Classifiers to be compared',
      name='staticTextClassifier', parent=self.panel1, pos=wx.Point(5, 36), size=wx.Size(131, 13), style=0)

    self.checkListBoxClassifiers = wx.CheckListBox(choices=[], id=wxID_DIALOGREPORT1CHECKLISTBOXCLASSIFIERS, name='checkListBoxClassifiers',
      parent=self.panel1, pos=wx.Point(146, 36), size=wx.Size(340, 167), style=0)

    self.staticTextReferenceClassifier = wx.StaticText(id=wxID_DIALOGREPORT1STATICTEXTREFERENCECLASSIFIER, label='Reference judge',
      name='staticTextReferenceClassifier', parent=self.panel1, pos=wx.Point(5, 5), size=wx.Size(95, 13), style=0)

    self.choiceClassifier = wx.Choice(choices=[], id=wxID_DIALOGREPORT1CHOICECLASSIFIER, name='choiceClassifier', parent=self.panel1,
      pos=wx.Point(146, 5), size=wx.Size(340, 21), style=0)

    self.buttonGenerate = wx.Button(id=wxID_DIALOGREPORT1BUTTONGENERATE, label='&Generate', name='buttonGenerate', parent=self, pos=wx.Point(501, 10),
      size=wx.Size(75, 23), style=0)
    self.buttonGenerate.Bind(wx.EVT_BUTTON, self.OnButtonGenerateButton, id=wxID_DIALOGREPORT1BUTTONGENERATE)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_choices()


  def read_data(self):
    self.cursor = t_colony.get_cursor_joined_score(session.session.idexperiment, self.idjudge)
    self.rows = self.cursor.rowcount
    self.cols = db_con.get_field_count(self.cursor)
    self.data = self.cursor.fetchall()


  def init_choices(self):
    self.data_cl = t_judge.get_all_data(("id", "name"))
    for (id, name) in self.data_cl:
      self.choiceClassifier.Append(name)
      self.checkListBoxClassifiers.Append(name)
   


  def OnButtonGenerateButton(self, event):
    
    index = self.choiceClassifier.GetSelection()
    if index < 0:
      output("No reference classifier was selected!", OUTPUT_ERROR)
      return
    else:
      idjudge = self.data_cl[index][0]
    
    idjudges = []
    for i in range(0, len(self.data_cl)):
      if self.checkListBoxClassifiers.IsChecked(i):
        idjudges.append(self.data_cl[i][0])

    if len(idjudges) == 0:
      output("No classifiers to be compared were selected.", OUTPUT_ERROR)
      return

    act_report2.generate(idjudge, idjudges)
    

    

