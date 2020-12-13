#Boa:Dialog:DialogReport1
import wx, wx.grid, db_con, session, act_report1

from table_colony import t_colony
from table_spectrum import t_spectrum
from table_judge import t_judge
from table_score import t_score
from table_series import t_series
from table_colony_judge import t_colony_judge
from table_deact_spectrum import t_deact_spectrum
from output import *
from errors import *
import act_report1
from judge import *
from chart import *
from series import *
from misc import paint_grid_row

def create(parent):
    return DialogReport1(parent)

dlg_chart = None

[wxID_DIALOGREPORT1, wxID_DIALOGREPORT1BUTTONACTIVATE, wxID_DIALOGREPORT1BUTTONCHART, wxID_DIALOGREPORT1BUTTONDEACTIVATE, 
 wxID_DIALOGREPORT1BUTTONGENERATE, wxID_DIALOGREPORT1BUTTONLOAD, wxID_DIALOGREPORT1CHECKLISTBOXCLASSIFIERS, wxID_DIALOGREPORT1GRID, 
 wxID_DIALOGREPORT1PANEL2, wxID_DIALOGREPORT1PANELLOAD, wxID_DIALOGREPORT1PANELTOOLS, wxID_DIALOGREPORT1STATICTEXTCLASSIFIER, 
] = [wx.NewId() for _init_ctrls in range(12)]


COLOUR_INACTIVE = "#CCCCCC"
COLOUR_ACTIVE = "#FFFFFF"
COLOUR_INVALID = "#FF0000"



class DialogReport1(wx.Dialog):
  def _init_coll_boxSizerBody_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panelLoad, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.panelTools, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.grid, 1, border=5, flag=wx.EXPAND | wx.ALL)

  def _init_coll_boxSizerLoad_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticTextClassifier, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.checkListBoxClassifiers, 1, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.panel2, 0, border=5, flag=wx.GROW | wx.ALL)

  def _init_coll_boxSizerLoadButtons_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonGenerate, 0, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.buttonLoad, 0, border=5, flag=wx.GROW | wx.ALL)

  def _init_coll_boxSizerTools_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonChart, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.buttonActivate, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.buttonDeactivate, 0, border=5, flag=wx.ALL)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizerBody = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerLoad = wx.BoxSizer(orient=wx.HORIZONTAL)
    self.boxSizerLoad.SetMinSize(wx.Size(538, 85))

    self.boxSizerLoadButtons = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerTools = wx.BoxSizer(orient=wx.HORIZONTAL)

    self._init_coll_boxSizerBody_Items(self.boxSizerBody)
    self._init_coll_boxSizerLoad_Items(self.boxSizerLoad)
    self._init_coll_boxSizerLoadButtons_Items(self.boxSizerLoadButtons)
    self._init_coll_boxSizerTools_Items(self.boxSizerTools)

    self.SetSizer(self.boxSizerBody)
    self.panelTools.SetSizer(self.boxSizerTools)
    self.panel2.SetSizer(self.boxSizerLoadButtons)
    self.panelLoad.SetSizer(self.boxSizerLoad)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGREPORT1, name='DialogReport1', parent=prnt, pos=wx.Point(481, 250), size=wx.Size(578, 362),
      style=wx.DEFAULT_FRAME_STYLE, title='Scan scores report')
    self.SetClientSize(wx.Size(562, 326))
    self.SetToolTipString('DialogTray')

    self.panelLoad = wx.Panel(id=wxID_DIALOGREPORT1PANELLOAD, name='panelLoad', parent=self, pos=wx.Point(0, 0), size=wx.Size(562, 83),
      style=wx.TAB_TRAVERSAL)
    self.panelLoad.SetMinSize(wx.Size(534, 83))

    self.staticTextClassifier = wx.StaticText(id=wxID_DIALOGREPORT1STATICTEXTCLASSIFIER, label='Classifiers to show', name='staticTextClassifier',
      parent=self.panelLoad, pos=wx.Point(5, 5), size=wx.Size(91, 13), style=0)

    self.checkListBoxClassifiers = wx.CheckListBox(choices=[], id=wxID_DIALOGREPORT1CHECKLISTBOXCLASSIFIERS, name='checkListBoxClassifiers',
      parent=self.panelLoad, pos=wx.Point(106, 5), size=wx.Size(315, 73), style=0)

    self.panel2 = wx.Panel(id=wxID_DIALOGREPORT1PANEL2, name='panel2', parent=self.panelLoad, pos=wx.Point(431, 5), size=wx.Size(126, 73),
      style=wx.TAB_TRAVERSAL)

    self.buttonGenerate = wx.Button(id=wxID_DIALOGREPORT1BUTTONGENERATE, label='&Generate Report', name='buttonGenerate', parent=self.panel2,
      pos=wx.Point(5, 5), size=wx.Size(116, 23), style=0)
    self.buttonGenerate.Bind(wx.EVT_BUTTON, self.OnButtonGenerateButton, id=wxID_DIALOGREPORT1BUTTONGENERATE)

    self.buttonLoad = wx.Button(id=wxID_DIALOGREPORT1BUTTONLOAD, label='&Load', name='buttonLoad', parent=self.panel2, pos=wx.Point(5, 38),
      size=wx.Size(116, 23), style=0)
    self.buttonLoad.Bind(wx.EVT_BUTTON, self.OnButtonLoadButton, id=wxID_DIALOGREPORT1BUTTONLOAD)

    self.grid = wx.grid.Grid(id=wxID_DIALOGREPORT1GRID, name='grid', parent=self, pos=wx.Point(5, 121), size=wx.Size(552, 200), style=0)
    self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnGridGridCellLeftDclick)
    self.grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.OnGridGridLabelLeftDclick)

    self.panelTools = wx.Panel(id=wxID_DIALOGREPORT1PANELTOOLS, name='panelTools', parent=self, pos=wx.Point(0, 83), size=wx.Size(562, 33),
      style=wx.TAB_TRAVERSAL)

    self.buttonChart = wx.Button(id=wxID_DIALOGREPORT1BUTTONCHART, label='Show &Chart', name='buttonChart', parent=self.panelTools, pos=wx.Point(5,
      5), size=wx.Size(75, 23), style=0)
    self.buttonChart.Bind(wx.EVT_BUTTON, self.OnButtonChartButton, id=wxID_DIALOGREPORT1BUTTONCHART)

    self.buttonActivate = wx.Button(id=wxID_DIALOGREPORT1BUTTONACTIVATE, label='&Activate', name='buttonActivate', parent=self.panelTools,
      pos=wx.Point(90, 5), size=wx.Size(75, 23), style=0)
    self.buttonActivate.Bind(wx.EVT_BUTTON, self.OnButtonActivateButton, id=wxID_DIALOGREPORT1BUTTONACTIVATE)

    self.buttonDeactivate = wx.Button(id=wxID_DIALOGREPORT1BUTTONDEACTIVATE, label='&Deactivate', name='buttonDeactivate', parent=self.panelTools,
      pos=wx.Point(175, 5), size=wx.Size(75, 23), style=0)
    self.buttonDeactivate.Bind(wx.EVT_BUTTON, self.OnButtonDeactivateButton, id=wxID_DIALOGREPORT1BUTTONDEACTIVATE)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_choices()

    self.flag_first_load = True
    self.flag_loaded = False
    
    self.sync_loaded()

  def sync_loaded(self):
    self.buttonChart.Enabled = self.flag_loaded
    self.buttonActivate.Enabled = self.flag_loaded
    self.buttonDeactivate.Enabled = self.flag_loaded
    

  def init_choices(self):
    self.data_cl = t_judge.get_all_data(("id", "name"))
    for (id, name) in self.data_cl:
      self.checkListBoxClassifiers.Append(name)


  def configure_grid_header(self):
    # This function is not general. Bad practice!
    self.grid.SetColLabelValue(0, "Id")
    self.grid.SetColLabelValue(1, "Tray")
    self.grid.SetColLabelValue(2, "Slide")
    self.grid.SetColLabelValue(3, "Colony")
    self.grid.SetColLabelValue(4, "File name")
    
    i = 0
    for name in act_report1.judge_names(self.idjudge_s):
      self.grid.SetColLabelValue(i+5, name)
      i += 1

  def read_data(self):
    self.data = act_report1.mount_data(self.idjudge_s)
    self.rows = len(self.data)
    if self.rows > 0:
      self.cols = len(self.data[0])-act_report1.NO_COLS_SKIP
    else:
      self.cols = 0

  def fill_grid(self):
    rows = self.grid.GetNumberRows()
    if rows > 0:
      self.grid.DeleteRows(0, rows)
    self.grid.AppendRows(self.rows)

    i = 0
    for row in self.data:
      # row is (flag_active, idspectrum, tray code, slide code, colony code, file name, ...)
      
      j = 0
      for value in row[act_report1.NO_COLS_SKIP:]:
        
        self.grid.SetCellValue(i, j, str(value))
        j += 1

      flag_active = row[1]
      if not flag_active:
        paint_grid_row(COLOUR_INACTIVE, self.grid, i)
      
      i += 1


  def init_grid(self):
    self.read_data()
    
    self.grid.CreateGrid(self.rows, self.cols, selmode=wx.grid.Grid.SelectRows)
    self.grid.EnableEditing(False)
    
    self.configure_grid_header()
    
    self.fill_grid()    



  def make_idjudges(self):
    idjudges = []
    for i in range(0, len(self.data_cl)):
      if self.checkListBoxClassifiers.IsChecked(i):
        idjudges.append(self.data_cl[i][0])

    if len(idjudges) == 0:
      raise error_x("No classifiers were selected.")
  
    self.idjudge_s = idjudges


  def call_chart(self, i):
    #return self.grid.GetGridCursorRow()
    
    idspectrum = self.data[i][1]
    idcolony = t_spectrum.get_value_from_id("idcolony", idspectrum)

    import act_main
    act_main.chart_colony(idcolony, idspectrum_selected=idspectrum)

  def process_sort(self, col_no):
    def compare(x, y):
      a = x[col_no+act_report1.NO_COLS_SKIP]
      b = y[col_no+act_report1.NO_COLS_SKIP]
      
      if a < b:
        return -1
      elif a > b:
        return 1
      return 0
      
    self.data.sort(compare)
    self.fill_grid()

  def OnButtonGenerateButton(self, event):
    self.make_idjudges()
    act_report1.generate(self.idjudge_s)


  def OnButtonLoadButton(self, event):
    self.make_idjudges()

    if self.flag_first_load:
      self.init_grid()
      self.flag_first_load = False

    self.flag_loaded = False
    self.read_data()
    self.fill_grid()  
    self.flag_loaded = True
    self.sync_loaded()  

  def get_row_no(self):
    return self.grid.GetGridCursorRow()
  
  def get_idspectrum(self):
    i = self.get_row_no()
    if i >= 0:
      return self.data[i][0]
    return -1

  def OnGridGridCellLeftDclick(self, event):
    self.call_chart(self.get_row_no())

  def OnGridGridLabelLeftDclick(self, event):
    self.process_sort(event.GetCol())

  def OnButtonChartButton(self, event):
    self.call_chart(self.get_row_no())

  def set_active(self, flag):
    row_no = self.get_row_no()
    if row_no > -1:
      idspectrum = self.get_idspectrum()
      t_deact_spectrum.set_flag_inactive(not flag, idspectrum, session.session.iddeact)
      paint_grid_row(COLOUR_INVALID, self.grid, row_no)
      
  def OnButtonActivateButton(self, event):
    self.set_active(1)

  def OnButtonDeactivateButton(self, event):
    self.set_active(0)

    
  
    

    
