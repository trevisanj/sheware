#Boa:Dialog:DialogTray
import wx
import wx.grid
import db_con
from session import *
from output import *
from errors import *
import DialogEditTray
from table_tray import t_tray
import act_tray
from table_experiment import t_experiment
from table_spectrum import t_spectrum
import act_main

def create(parent):
    return DialogTray(parent)

[wxID_DIALOGTRAY, wxID_DIALOGTRAYBUTTONDELETE, wxID_DIALOGTRAYBUTTONEDIT, wxID_DIALOGTRAYBUTTONINSERT, wxID_DIALOGTRAYBUTTONLOAD, 
 wxID_DIALOGTRAYBUTTONSLIDES, wxID_DIALOGTRAYCHOICE, wxID_DIALOGTRAYGRID, wxID_DIALOGTRAYPANELACTIONS, wxID_DIALOGTRAYPANELGRID, 
 wxID_DIALOGTRAYPANELTOP, wxID_DIALOGTRAYSTATICTEXTEXPERIMENT, 
] = [wx.NewId() for _init_ctrls in range(12)]

class DialogTray(wx.Dialog):
  def _init_coll_boxSizerMain_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panelTop, 0, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.panelActions, 0, border=5, flag=wx.GROW | wx.ALL)
    parent.AddWindow(self.panelGrid, 10, border=5, flag=wx.ALL | wx.GROW)

  def _init_coll_boxSizerGrid_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.grid, 10, border=0, flag=wx.GROW)

  def _init_coll_boxSizerTop_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticTextExperiment, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.choice, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.buttonLoad, 0, border=5, flag=wx.ALL)

  def _init_coll_boxSizerActions_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonInsert, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonEdit, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonDelete, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonSlides, 0, border=3, flag=wx.ALL)

  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizerMain = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerActions = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.boxSizerGrid = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizerTop = wx.BoxSizer(orient=wx.HORIZONTAL)

    self._init_coll_boxSizerMain_Items(self.boxSizerMain)
    self._init_coll_boxSizerActions_Items(self.boxSizerActions)
    self._init_coll_boxSizerGrid_Items(self.boxSizerGrid)
    self._init_coll_boxSizerTop_Items(self.boxSizerTop)

    self.SetSizer(self.boxSizerMain)
    self.panelActions.SetSizer(self.boxSizerActions)
    self.panelTop.SetSizer(self.boxSizerTop)
    self.panelGrid.SetSizer(self.boxSizerGrid)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGTRAY, name='DialogTray', parent=prnt, pos=wx.Point(449, 148), size=wx.Size(605, 494),
      style=wx.DIALOG_MODAL | wx.DEFAULT_DIALOG_STYLE | wx.DEFAULT_FRAME_STYLE, title='Trays')
    self.SetClientSize(wx.Size(589, 458))

    self.panelActions = wx.Panel(id=wxID_DIALOGTRAYPANELACTIONS, name='panelActions', parent=self, pos=wx.Point(5, 48), size=wx.Size(579, 29),
      style=wx.TAB_TRAVERSAL)

    self.panelGrid = wx.Panel(id=wxID_DIALOGTRAYPANELGRID, name='panelGrid', parent=self, pos=wx.Point(5, 87), size=wx.Size(579, 366),
      style=wx.TAB_TRAVERSAL)

    self.buttonInsert = wx.Button(id=wxID_DIALOGTRAYBUTTONINSERT, label='&Insert', name='buttonInsert', parent=self.panelActions, pos=wx.Point(3, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonInsert.Bind(wx.EVT_BUTTON, self.OnButtonInsertButton, id=wxID_DIALOGTRAYBUTTONINSERT)

    self.buttonEdit = wx.Button(id=wxID_DIALOGTRAYBUTTONEDIT, label='&Edit', name='buttonEdit', parent=self.panelActions, pos=wx.Point(84, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonEdit.Bind(wx.EVT_BUTTON, self.OnButtonEditButton, id=wxID_DIALOGTRAYBUTTONEDIT)

    self.buttonDelete = wx.Button(id=wxID_DIALOGTRAYBUTTONDELETE, label='&Delete', name='buttonDelete', parent=self.panelActions, pos=wx.Point(165,
      3), size=wx.Size(75, 23), style=0)
    self.buttonDelete.Bind(wx.EVT_BUTTON, self.OnButtonDeleteButton, id=wxID_DIALOGTRAYBUTTONDELETE)

    self.grid = wx.grid.Grid(id=wxID_DIALOGTRAYGRID, name='grid', parent=self.panelGrid, pos=wx.Point(0, 0), size=wx.Size(579, 366), style=0)
    self.grid.SetLabel('grid')
    self.grid.SetHelpText('')
    self.grid.SetToolTipString('grid')
    self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnGridGridCellLeftDclick)

    self.buttonSlides = wx.Button(id=wxID_DIALOGTRAYBUTTONSLIDES, label='&Slides...', name='buttonSlides', parent=self.panelActions, pos=wx.Point(246,
      3), size=wx.Size(75, 23), style=0)
    self.buttonSlides.Bind(wx.EVT_BUTTON, self.OnButtonSlidesButton, id=wxID_DIALOGTRAYBUTTONSLIDES)

    self.panelTop = wx.Panel(id=wxID_DIALOGTRAYPANELTOP, name='panelTop', parent=self, pos=wx.Point(5, 5), size=wx.Size(579, 33),
      style=wx.TAB_TRAVERSAL)

    self.staticTextExperiment = wx.StaticText(id=wxID_DIALOGTRAYSTATICTEXTEXPERIMENT, label='Experiment', name='staticTextExperiment',
      parent=self.panelTop, pos=wx.Point(5, 10), size=wx.Size(55, 13), style=0)

    self.choice = wx.Choice(choices=[], id=wxID_DIALOGTRAYCHOICE, name='choice', parent=self.panelTop, pos=wx.Point(70, 5), size=wx.Size(218, 21),
      style=0)

    self.buttonLoad = wx.Button(id=wxID_DIALOGTRAYBUTTONLOAD, label='&Load', name='buttonLoad', parent=self.panelTop, pos=wx.Point(298, 5),
      size=wx.Size(75, 23), style=0)
    self.buttonLoad.Bind(wx.EVT_BUTTON, self.OnButtonLoadButton, id=wxID_DIALOGTRAYBUTTONLOAD)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.flag_first_fill = True
    self.idexperiment = -1
    self.init_choices()
    
  def set_idexperiment(self, value):
    self.idexperiment = value
    
    flag = False
    i = 0
    for (id, name) in self.data_experiment:
      if id == value:
        flag = True
        self.choice.SetSelection(i)
      i += 1
    if not flag:
      raise error_x("Invalid idexperiment: %s" % value)
    
    self.read_data()
    self.fill_grid()
    
    
  def init_choices(self):
    self.data_experiment = t_experiment.get_cursor(("id", "name")).fetchall()
    for (id, name) in self.data_experiment:
      self.choice.Append(name)
    
  def read_data(self):
    #self.cursor = t_tray.get_cursor_1experiment_with_spectrum_count(("tray.id", "tray.code", "concat(substring(tray.comments, 1, 50), if(length(tray.comments) > 50, '...', '')) as comments", "count(spectrum.id) as spectra", "length(tray.picture) as picture_size"), self.idexperiment)
    
    self.cursor = t_spectrum.get_cursor_data(field_names=(
    "tray.id", 
    "tray.code", 
    "concat(substring(tray.comments, 1, 50), if(length(tray.comments) > 50, '...', '')) as comments", 
    "length(tray.picture) as picture_size",
    "count(spectrum.id) as spectra", 
    "sum(flag_inactive is null or flag_inactive = 0) as sum_active",
    "sum(flag_inactive is not null and flag_inactive = 1) as sum_inactive"
    ),
    groupbys=["tray.id"], flag_join_tray=True, iddeact=session.iddeact, idexperiment=self.idexperiment)

    

    self.rows = self.cursor.rowcount
    self.cols = db_con.get_field_count(self.cursor)
    self.data = self.cursor.fetchall()
    
  
  def fill_grid(self):
    if self.flag_first_fill:
      self.init_grid()
      self.flag_first_fill = False

    rows = self.grid.GetNumberRows()
    if rows > 0:
      self.grid.DeleteRows(0, rows)
    self.grid.AppendRows(self.rows)

    for i in range(0, self.rows):
      for j in range(0, self.cols):
        self.grid.SetCellValue(i, j, str(self.data[i][j]))
    self.grid.AutoSize()

  def init_grid(self):
    self.grid.CreateGrid(0, self.cols, selmode=wx.grid.Grid.SelectRows)
    self.grid.EnableEditing(False)
    
    col_names = db_con.get_field_names(self.cursor)
    for j in range(0, self.cols):
      self.grid.SetColLabelValue(j, col_names[j])
    
    
  def get_row(self):
    index = self.grid.GetGridCursorRow()
    if index >= 0:
      return self.data[index] #returns first (and only) selected row
    else:
      return None
    
  
  def insert(self):
    act_tray.insert(self.idexperiment)
    self.read_data()
    self.fill_grid()

  def edit(self):
    row = self.get_row()
    if row <> None:
      act_tray.edit(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("No data to edit.", OUTPUT_ERROR)

  def delete(self):
    row = self.get_row()
    if row <> None:
      act_tray.delete(row[0])
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

  def OnButtonSlidesButton(self, event):
    row = self.get_row()
    if row <> None:
      act_main.slide(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("No tray.", OUTPUT_ERROR)

  def OnButtonLoadButton(self, event):
    index = self.choice.GetSelection()
    if index < 0:
      output("Please select experiment first.", OUTPUT_ERROR)
    else:
      self.set_idexperiment(self.data_experiment[index][0])
