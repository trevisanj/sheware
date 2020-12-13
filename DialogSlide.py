#Boa:Dialog:DialogSlide
import wx
import wx.grid
import db_con
from output import *
from errors import *
import DialogEditSlide
from table_slide import t_slide
import act_slide
from table_tray import t_tray
import act_main
from session import *
from table_spectrum import t_spectrum

def create(parent):
    return DialogSlide(parent)

[wxID_DIALOGSLIDE, wxID_DIALOGSLIDEBUTTONDELETE, wxID_DIALOGSLIDEBUTTONEDIT, wxID_DIALOGSLIDEBUTTONINSERT, wxID_DIALOGSLIDEBUTTONLOAD, 
 wxID_DIALOGSLIDEBUTTONSLIDES, wxID_DIALOGSLIDECHOICE, wxID_DIALOGSLIDEGRID, wxID_DIALOGSLIDEPANELACTIONS, wxID_DIALOGSLIDEPANELGRID, 
 wxID_DIALOGSLIDEPANELTOP, wxID_DIALOGSLIDESTATICTEXTEXPERIMENT, 
] = [wx.NewId() for _init_ctrls in range(12)]

class DialogSlide(wx.Dialog):
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

    parent.AddWindow(self.staticTextTray, 0, border=5, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL)
    parent.AddWindow(self.choice, 0, border=5, flag=wx.ALL)
    parent.AddWindow(self.buttonLoad, 0, border=5, flag=wx.ALL)

  def _init_coll_boxSizerActions_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.buttonInsert, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonEdit, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonDelete, 0, border=3, flag=wx.ALL)
    parent.AddWindow(self.buttonColonies, 0, border=3, flag=wx.ALL)

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
    wx.Dialog.__init__(self, id=wxID_DIALOGSLIDE, name='DialogSlide', parent=prnt, pos=wx.Point(449, 148), size=wx.Size(605, 494),
      style=wx.DIALOG_MODAL | wx.DEFAULT_DIALOG_STYLE | wx.DEFAULT_FRAME_STYLE, title='Slides')
    self.SetClientSize(wx.Size(589, 458))

    self.panelActions = wx.Panel(id=wxID_DIALOGSLIDEPANELACTIONS, name='panelActions', parent=self, pos=wx.Point(5, 48), size=wx.Size(579, 29),
      style=wx.TAB_TRAVERSAL)

    self.panelGrid = wx.Panel(id=wxID_DIALOGSLIDEPANELGRID, name='panelGrid', parent=self, pos=wx.Point(5, 87), size=wx.Size(579, 366),
      style=wx.TAB_TRAVERSAL)

    self.buttonInsert = wx.Button(id=wxID_DIALOGSLIDEBUTTONINSERT, label='&Insert', name='buttonInsert', parent=self.panelActions, pos=wx.Point(3, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonInsert.Bind(wx.EVT_BUTTON, self.OnButtonInsertButton, id=wxID_DIALOGSLIDEBUTTONINSERT)

    self.buttonEdit = wx.Button(id=wxID_DIALOGSLIDEBUTTONEDIT, label='&Edit', name='buttonEdit', parent=self.panelActions, pos=wx.Point(84, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonEdit.Bind(wx.EVT_BUTTON, self.OnButtonEditButton, id=wxID_DIALOGSLIDEBUTTONEDIT)

    self.buttonDelete = wx.Button(id=wxID_DIALOGSLIDEBUTTONDELETE, label='&Delete', name='buttonDelete', parent=self.panelActions, pos=wx.Point(165,
      3), size=wx.Size(75, 23), style=0)
    self.buttonDelete.Bind(wx.EVT_BUTTON, self.OnButtonDeleteButton, id=wxID_DIALOGSLIDEBUTTONDELETE)

    self.grid = wx.grid.Grid(id=wxID_DIALOGSLIDEGRID, name='grid', parent=self.panelGrid, pos=wx.Point(0, 0), size=wx.Size(579, 366), style=0)
    self.grid.SetLabel('grid')
    self.grid.SetHelpText('')
    self.grid.SetToolTipString('grid')
    self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnGridGridCellLeftDclick)

    self.buttonColonies = wx.Button(id=wxID_DIALOGSLIDEBUTTONSLIDES, label='&Colonies...', name='buttonColonies', parent=self.panelActions, pos=wx.Point(246,
      3), size=wx.Size(75, 23), style=0)
    self.buttonColonies.Bind(wx.EVT_BUTTON, self.OnButtonColoniesButton, id=wxID_DIALOGSLIDEBUTTONSLIDES)

    self.panelTop = wx.Panel(id=wxID_DIALOGSLIDEPANELTOP, name='panelTop', parent=self, pos=wx.Point(5, 5), size=wx.Size(579, 33),
      style=wx.TAB_TRAVERSAL)

    self.staticTextTray = wx.StaticText(id=wxID_DIALOGSLIDESTATICTEXTEXPERIMENT, label='Tray', name='staticTextTray',
      parent=self.panelTop, pos=wx.Point(5, 10), size=wx.Size(55, 13), style=0)

    self.choice = wx.Choice(choices=[], id=wxID_DIALOGSLIDECHOICE, name='choice', parent=self.panelTop, pos=wx.Point(70, 5), size=wx.Size(218, 21),
      style=0)

    self.buttonLoad = wx.Button(id=wxID_DIALOGSLIDEBUTTONLOAD, label='&Load', name='buttonLoad', parent=self.panelTop, pos=wx.Point(298, 5),
      size=wx.Size(75, 23), style=0)
    self.buttonLoad.Bind(wx.EVT_BUTTON, self.OnButtonLoadButton, id=wxID_DIALOGSLIDEBUTTONLOAD)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.flag_first_fill = True
    self.idtray = -1
  
  def set_idexperiment(self, value):
    self.idexperiment = value
    self.init_choices()
    
  def set_idtray(self, value):
    self.idtray = value
    
    flag = False
    i = 0
    for (id, code) in self.data_tray:
      if id == value:
        flag = True
        self.choice.SetSelection(i)
      i += 1
    if not flag:
      raise error_x("Invalid idtray: %s" % value)
    
    self.read_data()
    self.fill_grid()
    
    
  def init_choices(self):
    self.data_tray = t_tray.get_cursor_1experiment(("id", "code"), self.idexperiment).fetchall()
    for (id, code) in self.data_tray:
      self.choice.Append(code)
    
  def read_data(self):
    #self.cursor = t_slide.get_cursor_1tray_with_spectrum_count(("slide.id", "slide.code", "concat(substring(slide.comments, 1, 50), if(length(slide.comments) > 50, '...', '')) as comments", "count(spectrum.id) as spectra", "length(slide.picture) as picture_size"), self.idtray)
    
    self.cursor = t_spectrum.get_cursor_data(field_names=(
    "slide.id", 
    "slide.code", 
    "concat(substring(slide.comments, 1, 50), if(length(slide.comments) > 50, '...', '')) as comments", 
    "count(spectrum.id) as spectra", 
    "sum(flag_inactive is null or flag_inactive = 0) as sum_active",
    "sum(flag_inactive is not null and flag_inactive = 1) as sum_inactive"
    ),
    groupbys=["slide.id"], flag_join_tray=True, iddeact=session.iddeact, idtray=self.idtray)

    
    
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
    act_slide.insert(self.idtray)
    self.read_data()
    self.fill_grid()

  def edit(self):
    row = self.get_row()
    if row <> None:
      act_slide.edit(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("No data to edit.", OUTPUT_ERROR)

  def delete(self):
    row = self.get_row()
    if row <> None:
      act_slide.delete(row[0])
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

  def OnButtonColoniesButton(self, event):
    row = self.get_row()
    if row <> None:
      act_main.colony(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("No slide.", OUTPUT_ERROR)

  def OnButtonLoadButton(self, event):
    index = self.choice.GetSelection()
    if index < 0:
      output("Please select tray first.", OUTPUT_ERROR)
    else:
      self.set_idtray(self.data_tray[index][0])
