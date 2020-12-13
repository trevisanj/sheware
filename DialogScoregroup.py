#Boa:Dialog:DialogScoregroup
import wx
import wx.grid
import db_con
import session
from table_score import t_score
from output import *
from errors import *
import DialogEditScoregroup
from table_scoregroup import t_scoregroup
import act_scoregroup

def create(parent):
    return DialogScoregroup(parent)

[wxID_DIALOGSCOREGROUP, wxID_DIALOGSCOREGROUPBUTTONDELETE, wxID_DIALOGSCOREGROUPBUTTONEDIT, wxID_DIALOGSCOREGROUPBUTTONINSERT, 
 wxID_DIALOGSCOREGROUPGRID, wxID_DIALOGSCOREGROUPPANEL1, wxID_DIALOGSCOREGROUPPANEL2, 
] = [wx.NewId() for _init_ctrls in range(7)]

class DialogScoregroup(wx.Dialog):
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
    wx.Dialog.__init__(self, id=wxID_DIALOGSCOREGROUP, name='DialogScoregroup', parent=prnt, pos=wx.Point(426, 194), size=wx.Size(504, 494),
      style=wx.DIALOG_MODAL | wx.DEFAULT_DIALOG_STYLE | wx.DEFAULT_FRAME_STYLE, title='Score groups')
    self.SetClientSize(wx.Size(488, 458))

    self.panel1 = wx.Panel(id=wxID_DIALOGSCOREGROUPPANEL1, name='panel1', parent=self, pos=wx.Point(5, 5), size=wx.Size(478, 29),
      style=wx.TAB_TRAVERSAL)

    self.panel2 = wx.Panel(id=wxID_DIALOGSCOREGROUPPANEL2, name='panel2', parent=self, pos=wx.Point(5, 44), size=wx.Size(478, 409),
      style=wx.TAB_TRAVERSAL)

    self.buttonInsert = wx.Button(id=wxID_DIALOGSCOREGROUPBUTTONINSERT, label='&Insert', name='buttonInsert', parent=self.panel1, pos=wx.Point(3, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonInsert.Bind(wx.EVT_BUTTON, self.OnButtonInsertButton, id=wxID_DIALOGSCOREGROUPBUTTONINSERT)

    self.buttonEdit = wx.Button(id=wxID_DIALOGSCOREGROUPBUTTONEDIT, label='&Edit', name='buttonEdit', parent=self.panel1, pos=wx.Point(84, 3),
      size=wx.Size(75, 23), style=0)
    self.buttonEdit.Bind(wx.EVT_BUTTON, self.OnButtonEditButton, id=wxID_DIALOGSCOREGROUPBUTTONEDIT)

    self.buttonDelete = wx.Button(id=wxID_DIALOGSCOREGROUPBUTTONDELETE, label='&Delete', name='buttonDelete', parent=self.panel1, pos=wx.Point(165,
      3), size=wx.Size(75, 23), style=0)
    self.buttonDelete.Bind(wx.EVT_BUTTON, self.OnButtonDeleteButton, id=wxID_DIALOGSCOREGROUPBUTTONDELETE)

    self.grid = wx.grid.Grid(id=wxID_DIALOGSCOREGROUPGRID, name='grid', parent=self.panel2, pos=wx.Point(0, 0), size=wx.Size(478, 409), style=0)
    self.grid.SetLabel('grid')
    self.grid.SetHelpText('')
    self.grid.SetToolTipString('grid')
    self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnGridGridCellLeftDclick)

    self._init_sizers()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_grid()
    

  def read_data(self):
    self.cursor = t_scoregroup.get_cursor()
    self.rows = self.cursor.rowcount
    self.cols = db_con.get_field_count(self.cursor)+1
    _data = self.cursor.fetchall()
    
    self.data = []
    for row in _data:
      self.data.append(row+(t_score.get_string_1scoregroup(row[0]),))

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
    for j in range(0, self.cols-1):
      self.grid.SetColLabelValue(j, col_names[j])
    self.grid.SetColLabelValue(self.cols-1, "score")

    self.fill_grid()    
    
    
  def get_row(self):
    index = self.grid.GetGridCursorRow()
    if index >= 0:
      return self.data[index] #returns first (and only) selected row
    else:
      return None
    
  
  def insert(self):
    act_scoregroup.insert()
    self.read_data()
    self.fill_grid()

  def edit(self):
    row = self.get_row()
    if row <> None:
      act_scoregroup.edit(row[0])
      self.read_data()
      self.fill_grid()
    else:
      output("No data to edit.", OUTPUT_ERROR)

  def delete(self):
    row = self.get_row()
    if row <> None:
      act_scoregroup.delete(row[0])
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
