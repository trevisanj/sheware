#Boa:Dialog:DialogExperiment
import wx
import wx.grid
import db_con
from session import *
from output import *
from errors import *
import DialogEditExperiment
from table_experiment import t_experiment
import act_experiment
import act_main
from table_spectrum import t_spectrum

def create(parent):
    return DialogExperiment(parent)

[wxID_DIALOGEXPERIMENT, wxID_DIALOGEXPERIMENTBUTTONDELETE, wxID_DIALOGEXPERIMENTBUTTONEDIT, wxID_DIALOGEXPERIMENTBUTTONINSERT, 
 wxID_DIALOGEXPERIMENTBUTTONTRAYS, wxID_DIALOGEXPERIMENTGRID, wxID_DIALOGEXPERIMENTPANEL1, wxID_DIALOGEXPERIMENTPANEL2, 
] = [wx.NewId() for _init_ctrls in range(8)]

class DialogExperiment(wx.Dialog):
  def _init_coll_boxSizer3_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.grid, 10, border=0, flag=wx.GROW)

  def _init_coll_boxSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panel1, 0, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.panel2, 10, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizer2_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonInsert, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonEdit, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonDelete, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonTrays, 0, border=3, flag=wx.ALL)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer2 = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.boxSizer3 = wx.BoxSizer(orient=wx.VERTICAL)

    self._init_coll_boxSizer1_Items(self.boxSizer1)
    self._init_coll_boxSizer2_Items(self.boxSizer2)
    self._init_coll_boxSizer3_Items(self.boxSizer3)

    self.SetSizer(self.boxSizer1)
    self.panel1.SetSizer(self.boxSizer2)
    self.panel2.SetSizer(self.boxSizer3)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGEXPERIMENT, name='DialogExperiment', parent=prnt, pos=wx.Point(504, 230), size=wx.Size(504, 494),
      style=wx.DIALOG_MODAL | wx.DEFAULT_DIALOG_STYLE | wx.DEFAULT_FRAME_STYLE, title='Experiments')
    self.SetClientSize(wx.Size(488, 458))

    self.panel1 = wx.Panel(id=wxID_DIALOGEXPERIMENTPANEL1, name='panel1', parent=self, pos=wx.Point(5, 5), size=wx.Size(478, 29),
      style=wx.TAB_TRAVERSAL)

    self.panel2 = wx.Panel(id=wxID_DIALOGEXPERIMENTPANEL2, name='panel2', parent=self, pos=wx.Point(5, 44), size=wx.Size(478, 409),
      style=wx.TAB_TRAVERSAL)

    self.buttonInsert = wx.Button(id=wxID_DIALOGEXPERIMENTBUTTONINSERT, label='&Insert', name='buttonInsert', parent=self.panel1, pos=wx.Point(3, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonInsert.Bind(wx.EVT_BUTTON, self.OnButtonInsertButton, id=wxID_DIALOGEXPERIMENTBUTTONINSERT)

    self.buttonEdit = wx.Button(id=wxID_DIALOGEXPERIMENTBUTTONEDIT, label='&Edit', name='buttonEdit', parent=self.panel1, pos=wx.Point(84, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonEdit.Bind(wx.EVT_BUTTON, self.OnButtonEditButton, id=wxID_DIALOGEXPERIMENTBUTTONEDIT)

    self.buttonDelete = wx.Button(id=wxID_DIALOGEXPERIMENTBUTTONDELETE, label='&Delete', name='buttonDelete', parent=self.panel1, pos=wx.Point(165,
      3), size=wx.Size(75, 23), style=0)
    self.buttonDelete.Bind(wx.EVT_BUTTON, self.OnButtonDeleteButton, id=wxID_DIALOGEXPERIMENTBUTTONDELETE)

    self.grid = wx.grid.Grid(id=wxID_DIALOGEXPERIMENTGRID, name='grid', parent=self.panel2, pos=wx.Point(0, 0), size=wx.Size(478, 409), style=0)
    self.grid.SetLabel('grid')
    self.grid.SetHelpText('')
    self.grid.SetToolTipString('grid')
    self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnGridGridCellLeftDclick)

    self.buttonTrays = wx.Button(id=wxID_DIALOGEXPERIMENTBUTTONTRAYS, label='&Trays...', name='buttonTrays', parent=self.panel1, pos=wx.Point(246, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonTrays.Bind(wx.EVT_BUTTON, self.OnButtonTraysButton, id=wxID_DIALOGEXPERIMENTBUTTONTRAYS)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_grid()
    

  def read_data(self):
    self.cursor = t_spectrum.get_cursor_data(field_names=(
    "experiment.id", "experiment.name", "experiment.date", 
    "concat(substring(experiment.comments, 1, 50), if(length(experiment.comments) > 50, '...', '')) as comments", 
    "count(spectrum.id) as spectra", 
    "sum(flag_inactive is null or flag_inactive = 0) as sum_active",
    "sum(flag_inactive is not null and flag_inactive = 1) as sum_inactive"
    ),
    groupbys=["spectrum.idexperiment"], flag_join_experiment=True, iddeact=session.iddeact)
    
    self.rows = self.cursor.rowcount
    self.cols = db_con.get_field_count(self.cursor)
    self.data = self.cursor.fetchall()
    

  def fill_grid(self):
    rows = self.grid.GetNumberRows()
    if rows > 0:
      self.grid.DeleteRows(0, rows)
    self.grid.AppendRows(self.rows)
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        self.grid.SetCellValue(i, j, str(self.data[i][j]))
    self.grid.AutoSize()

  def init_grid(self):
    self.read_data()
    
    self.grid.CreateGrid(0, self.cols, selmode=wx.grid.Grid.SelectRows)
    self.grid.EnableEditing(False)
    
    col_names = db_con.get_field_names(self.cursor)
    for j in range(0, self.cols):
      self.grid.SetColLabelValue(j, col_names[j])

    self.fill_grid()    
    
    
  def get_row(self):
    index = self.grid.GetGridCursorRow()
    if index >= 0:
      return self.data[index] #returns first (and only) selected row
    else:
      return None
    
  
  def insert(self):
    act_experiment.insert()
    self.read_data()
    self.fill_grid()

  def edit(self):
    row = self.get_row()
    if row <> None:
      act_experiment.edit(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("No data to edit.", OUTPUT_ERROR)

  def delete(self):
    row = self.get_row()
    if row <> None:
      act_experiment.delete(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("Nothing to delete.", OUTPUT_ERROR)

  def OnButtonInsertButton(self, event):
    self.insert()

  def OnButtonEditButton(self, event):
    self.edit()

  def OnButtonDeleteButton(self, event):
    self.delete()

  def OnGridGridCellLeftDclick(self, event):
    self.edit()

  def OnButtonTraysButton(self, event):
    row = self.get_row()
    if row <> None:
      act_main.tray(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("No experiment.", OUTPUT_ERROR)
