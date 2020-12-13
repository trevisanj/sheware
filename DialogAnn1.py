#Boa:Dialog:DialogAnn
#Boa:Dialog:DialogAnn

import wx
import wx.lib.buttons
import wx.lib.floatcanvas.FloatCanvas as fc
import wx.lib.floatcanvas.NavCanvas as nc
import os.path
import pair
from output import *
from table_tray import t_tray
from table_slide import t_slide
from table_setup import t_setup
from table_spectrum import t_spectrum
from table_series import t_series
from session import session
from errors import *
from chart import *
from series import *
from misc import *

ANN_NOTHING = 0
ANN_TRAY = 1
ANN_SLIDE = 2

TOOL_NONE = 0
TOOL_ELLIPSE = 1
TOOL_RECTANGLE = 2

ACTION_NONE = 0
ACTION_DEFINING = 1  # defining new object
ACTION_SELECTED = 2

COLOR_DEFINING = "Green"
COLOR_CURRENT = "Red"
COLOR_DISABLED = "Gray"



def create(parent):
  return DialogAnn(parent)

[wxID_DIALOGANN, wxID_DIALOGANNBUTTON1, wxID_DIALOGANNGENTOGGLEBUTTON1, wxID_DIALOGANNGENTOGGLEBUTTON2, wxID_DIALOGANNLISTBOX1, 
 wxID_DIALOGANNLISTBOX2, wxID_DIALOGANNLISTBOX3, wxID_DIALOGANNPANEL1, wxID_DIALOGANNPANEL2, wxID_DIALOGANNPANEL3, wxID_DIALOGANNPANEL4, 
 wxID_DIALOGANNPANEL5, wxID_DIALOGANNPANELPICTUREFRAME, wxID_DIALOGANNSTATICTEXT1, wxID_DIALOGANNSTATICTEXT2, wxID_DIALOGANNSTATICTEXT3, 
 wxID_DIALOGANNSTATICTEXT4, 
] = [wx.NewId() for _init_ctrls in range(17)]

wxID_DIALOGANNPANELPICTURE = wx.NewId()


dlg_chart = None

class DialogAnn(wx.Dialog):
  idtray = -1
  idslide = -1
  idcolony = -1
  
  flag_picture = False # Has a loaded picture in panelPicture?
  
  picture = None
  pairtemp = None
  pairss = []
  pairs = None
  coords_ini = None

  what_ann = ANN_NOTHING
  what_tool = TOOL_NONE
  what_action = ACTION_NONE # action in the canvas

  def _init_coll_boxSizer4_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panel5, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.staticText3, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.panelPictureFrame, 1, border=10, flag=wx.GROW)

  def _init_coll_boxSizer5_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.button1, 0, border=0, flag=0)
    parent.AddWindow(self.genToggleButton1, 0, border=0, flag=0)
    parent.AddWindow(self.genToggleButton2, 0, border=0, flag=0)

  def _init_coll_boxSizer3_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.staticText1, 0, border=3, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.listBox1, 10, border=0, flag=wx.GROW)
    parent.AddWindow(self.staticText2, 0, border=3, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.listBox2, 17, border=0, flag=wx.GROW)
    parent.AddWindow(self.staticText4, 0, border=3, flag=wx.ALL | wx.GROW)
    parent.AddWindow(self.listBox3, 10, border=0, flag=wx.GROW)

  def _init_coll_boxSizer1_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panel1, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.panel2, 1, border=0, flag=wx.GROW)

  def _init_coll_boxSizer2_Items(self, parent):
    # generated method, don't edit

    parent.AddWindow(self.panel3, 0, border=0, flag=wx.GROW)
    parent.AddWindow(self.panel4, 1, border=0, flag=wx.GROW)

  def status(s):
    pass
  

  def get_canvas_coords(self, event):
    """Tronsforms pixel coordinates inside the floatcanvas control to floatcanvas coordinates."""
    return self.canvas.PixelToWorld(event.GetPosition())

  def get_hit_coords(self, obj):
    return self.canvas.PixelToWorld(obj.HitCoords)
  
  def set_action(self, action):
    self.what_action = action

  ############################################################
  ## shape modification layer
      

  def bind_pair(self, pair):
    pair.shape.Bind(fc.EVT_FC_LEFT_DOWN, self.OnShapeDown)

  def unbind_pair(self, pair):
    pair.shape.UnBindAll()


  ############################################################
  ## State machine arrows
      
  def create_object(self, coords, s):
    self.coords_ini = coords
    p = pair.pair()
    if self.what_tool == TOOL_ELLIPSE:
      p.ellipse(coords, (0, 0), s)
    else:
      p.rectangle(coords, (0, 0), s)
    p.configure_style("defining")
    self.pairtemp = p
    self.add_pair_to_canvas(p)
    self.canvas.Draw(Force=True)
    self.set_action(ACTION_DEFINING)
      
  def cancel_defining(self):
    self.remove_pair_from_canvas(self.pairtemp)
    self.pairtemp = None
    self.canvas.Draw(Force=True)
    self.set_action(ACTION_NONE)
    
  def cancel_selected(self):
    self.pairtemp.configure_style("active")
    self.pairtemp = None
    self.canvas.Draw(Force=True)
    self.set_action(ACTION_NONE)
  
  def cancel_action(self):
    if self.what_action == ACTION_DEFINING:
      self.cancel_defining()
    elif self.what_action == ACTION_SELECTED:
      self.cancel_selected()     
    

  def confirm_defining(self):
    self.pairs.pairs.append(self.pairtemp)
    self.bind_pair(self.pairtemp)
    self.pairtemp.configure_style("selected")
    self.canvas.Draw(Force=True)
    self.set_action(ACTION_SELECTED)
    

  def resize_shape(self, xy, wh):
    self.pairtemp.change_xywh(xy, wh)
    self.canvas.Draw(Force=True)

  def delete_pair(self):
    obj = self.pairtemp
    self.cancel_selected()
    self.pairs.pairs.remove(obj)
    self.remove_pair_from_canvas(obj)
    self.canvas.Draw(Force=True)

  def change_index(self, i):
    self.cancel_action()
    if self.pairs <> None:
      for pair in self.pairs.pairs:
        pair.configure_style("inactive")
        self.unbind_pair(pair)
    self.pairs = self.pairss[i]
    for pair in self.pairs.pairs:
      pair.configure_style("active")
      self.bind_pair(pair)
    self.redraw()
    
  def call_chart(self, i):
    import act_main
    idcolony = self.pairss[i].id_
    act_main.chart_colony(idcolony)

  ################
  # over canvas...

  def redraw(self):
    self.canvas.Draw(Force=True)

  def canvas_initialize(self):
    self.canvas.InitAll()
    self.pairs = None
    self.pairss = []
    self.pairs = None
    self.pairtemp = None
    self.flag_picture = False

  def load_picture(self, table, id_):
    """Loads picture from database and puts it into the canvas."""
    
    # Picture...
    blob_img = table.get_value_from_id("picture", id_)

    if blob_img <> None:
      import cStringIO
      img = wx.ImageFromStream(cStringIO.StringIO(blob_img), wx.BITMAP_TYPE_ANY)
      bmp = img.ConvertToBitmap()

      self.picture = self.canvas.AddScaledBitmap(bmp, (0, 0), Position="tl", Height=img.GetHeight())

      self.picture.Bind(fc.EVT_FC_LEFT_DOWN, self.OnPictureLeftDown)
      self.picture.Bind(fc.EVT_FC_LEFT_UP, self.OnPictureLeftUp)

      self.flag_picture = True
    
  def load_picture_tray(self):
    """Wrapper over load_picture"""
    
    self.load_picture(t_tray, self.idtray)
    
  def load_picture_slide(self):
    """Wrapper over load_picture"""
    
    self.load_picture(t_slide, self.idslide)

  def add_pair_to_canvas(self, pair):
    self.canvas.AddObject(pair.shape)
    self.canvas.AddObject(pair.text)         

  def add_pairs_to_canvas(self, pairs):
    for pair in pairs.pairs:
      self.canvas.AddObject(pair.shape)
      self.canvas.AddObject(pair.text)         

  def remove_pair_from_canvas(self, p):
    self.canvas.RemoveObject(p.shape)
    self.canvas.RemoveObject(p.text)
    self.canvas.Draw(Force=True)

  def add_pairss_to_canvas(self):
    for pairs in self.pairss:
      self.add_pairs_to_canvas(pairs)

  ####################
  # Listbox dumb layer

  def append_row(self, listbox, id_, caption1, caption2, shapes, table):
    listbox.Append(caption1)
    
    p = pair.pairs(table=table, id_=id_, caption=caption1)
    p.from_string(shapes, caption2)
    self.pairss.append(p)

  def fill_listbox1(self):
    
    cursor = t_tray.get_cursor_1experiment(("id", "code"), session.idexperiment)
    
    self.data_tray = cursor.fetchall()
    rows = cursor.rowcount
    for i in range(0, rows):
      self.listBox1.Append(self.data_tray[i][1])
  
  def fill_listbox2(self):
    from table_slide import t_slide
    
    cursor = t_slide.get_cursor_1tray(("id", "code", "shapes"), self.idtray)
    self.data_slide = cursor.fetchall()

    self.clean_listbox2()
    
    rows = cursor.rowcount
    for i in range(0, rows):
      r = self.data_slide[i]
      self.append_row(self.listBox2, r[0], r[1], r[1], r[2], t_slide)
      
  def fill_listbox3(self):
    from table_colony import t_colony

    slide_code = t_slide.get_value_from_id("code", self.idslide)
    
    self.data_colony = t_spectrum.get_cursor_data(field_names=(
    "colony.id", 
    "colony.code", 
    "colony.shapes", 
    "sum(flag_inactive is null or flag_inactive = 0) as sum_active",
    "sum(flag_inactive is not null and flag_inactive = 1) as sum_inactive"
    ), \
    idslide=self.idslide,
    iddeact=session.iddeact,
    flag_join_colony=True, # this is a bonus to get_cursor_data() because it cannot find this out by itself
    groupbys=["colony.id"]).fetchall()

    self.clean_listbox3()
    
    rows = len(self.data_colony)
    for i in range(0, rows):
      r = self.data_colony[i]
      
      s = "%s: %s active" % (r[1], r[3])
      if int(r[4]) > 0:
        s += "; %s inactive" % r[4]
      
      self.append_row(self.listBox3, r[0], s, code_in_canvas(r[1], slide_code), r[2], t_colony)
      

  def clean_listbox2(self):
    self.listBox2.SetItems([])

  def clean_listbox3(self):
    self.listBox3.SetItems([])


  #########################
  ## Listbox business layer

  def save(self):
    for pairs in self.pairss:
      pairs.save()

  def change_tray(self, _idtray):
    self.cancel_action()
    self.save()
    
    self.canvas_initialize()

    self.idtray = _idtray
    self.idslide = -1
    self.what_ann = ANN_TRAY
    self.fill_listbox2()
    self.clean_listbox3()
    self.load_picture_tray()
    self.add_pairss_to_canvas()
    self.canvas.ZoomToBB()
    self.canvas.Draw(Force=True)

  def change_slide(self, _idslide):  
    self.cancel_action()
    self.save()

    self.canvas_initialize()

    self.idslide = _idslide
    self.idcolony = -1
    self.what_ann = ANN_SLIDE
    self.fill_listbox3()
    self.load_picture_slide()
    self.add_pairss_to_canvas()
    self.canvas.ZoomToBB()
    self.canvas.Draw(Force=True)


  ######################
  # Shape event handlers

  def OnShapeDown(self, obj):
    self.cancel_action()
    self.pairtemp = obj.pair
    self.pairtemp.configure_style("selected")
    self.set_action(ACTION_SELECTED)
    self.canvas.Draw(Force=True)

  def process_key_event(self, event):
    """Didn't know how to catch key events correctly. Arrows made the canvas loose focus rather than trigger events.
    
    Only delete works.
    
    However, the logic is correct. If I discover how to catch up the arrow keys, I can activate the resize feature.
    
    """
    flag = False # Key caught?
    if self.what_action == ACTION_SELECTED:

      key = event.GetKeyCode()

      if key == wx.WXK_DELETE:
        self.delete_pair()
        flag = True; 
      elif False and key in (wx.WXK_DOWN, wx.WXK_UP, wx.WXK_LEFT, wx.WXK_RIGHT):
        modifiers = event.GetModifiers()
        (x, y) = self.pairtemp.XY
        (w, h) = self.pairtemp.WH
        
        # Assures origin is bottom left and width and height are positive
        if w < 0: x += w; w = -w
        if h < 0: y += h; h = -h
          
        inc = 3
        if modifiers == wx.MOD_CONTROL:
          if key == wx.WXK_DOWN: flag = True; h += inc; y -=inc
          elif key == wx.WXK_UP: flag = True; h += inc
          elif key == wx.WXK_LEFT: flag = True; w += inc; x -= inc
          elif key == wx.WXK_RIGHT: flag = True; w += inc
        elif modifiers == wx.MOD_ALT:
          if key == wx.WXK_DOWN: flag = True; h -= inc
          elif key == wx.WXK_UP: flag = True; h -= inc; y += inc
          elif key == wx.WXK_LEFT: flag = True; w -= inc
          elif key == wx.WXK_RIGHT: flag = True; w -= inc; x += inc
          
        if flag:
          self.resize_shape((x, y), (w, h))
          
    if not flag:
      event.Skip()








  #########################################################################################################################################
  # AUTO-GENERATED METHODS

  
  def _init_sizers(self):
    # generated method, don't edit
    self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer2 = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.boxSizer3 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer4 = wx.BoxSizer(orient=wx.VERTICAL)

    self.boxSizer5 = wx.BoxSizer(orient=wx.HORIZONTAL)

    self.boxSizer6 = wx.BoxSizer(orient=wx.VERTICAL)

    self._init_coll_boxSizer1_Items(self.boxSizer1)
    self._init_coll_boxSizer2_Items(self.boxSizer2)
    self._init_coll_boxSizer3_Items(self.boxSizer3)
    self._init_coll_boxSizer4_Items(self.boxSizer4)
    self._init_coll_boxSizer5_Items(self.boxSizer5)

    self.SetSizer(self.boxSizer1)
    self.panelPictureFrame.SetSizer(self.boxSizer6)
    self.panel2.SetSizer(self.boxSizer2)
    self.panel3.SetSizer(self.boxSizer3)
    self.panel4.SetSizer(self.boxSizer4)
    self.panel5.SetSizer(self.boxSizer5)

  def _init_ctrls(self, prnt):
    # generated method, don't edit
    wx.Dialog.__init__(self, id=wxID_DIALOGANN, name='DialogAnn', parent=prnt, pos=wx.Point(152, 66), size=wx.Size(995, 734),
      style=wx.RESIZE_BORDER | wx.DEFAULT_FRAME_STYLE, title='Annotate')
    self.SetClientSize(wx.Size(987, 707))
    self.Center(wx.BOTH)
    self.Bind(wx.EVT_CLOSE, self.OnDialogAnnClose)

    self.panel1 = wx.Panel(id=wxID_DIALOGANNPANEL1, name='panel1', parent=self, pos=wx.Point(0, 0), size=wx.Size(987, 32), style=wx.TAB_TRAVERSAL)

    self.panel2 = wx.Panel(id=wxID_DIALOGANNPANEL2, name='panel2', parent=self, pos=wx.Point(0, 32), size=wx.Size(987, 675), style=wx.TAB_TRAVERSAL)

    self.panel3 = wx.Panel(id=wxID_DIALOGANNPANEL3, name='panel3', parent=self.panel2, pos=wx.Point(0, 0), size=wx.Size(176, 675),
      style=wx.TAB_TRAVERSAL)

    self.panel4 = wx.Panel(id=wxID_DIALOGANNPANEL4, name='panel4', parent=self.panel2, pos=wx.Point(176, 0), size=wx.Size(811, 675),
      style=wx.TAB_TRAVERSAL)

    self.listBox1 = wx.ListBox(choices=[], id=wxID_DIALOGANNLISTBOX1, name='listBox1', parent=self.panel3, pos=wx.Point(0, 19), size=wx.Size(176,
      167), style=0)
    self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox, id=wxID_DIALOGANNLISTBOX1)
    self.listBox1.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBox1ListboxDclick, id=wxID_DIALOGANNLISTBOX1)
    self.listBox1.Bind(wx.EVT_KEY_DOWN, self.OnListBox1KeyDown)
    self.listBox1.Bind(wx.EVT_CHAR, self.OnListBox1Char)

    self.listBox2 = wx.ListBox(choices=[], id=wxID_DIALOGANNLISTBOX2, name='listBox2', parent=self.panel3, pos=wx.Point(0, 205), size=wx.Size(176,
      283), style=0)
    self.listBox2.Bind(wx.EVT_LISTBOX, self.OnListBox2Listbox, id=wxID_DIALOGANNLISTBOX2)
    self.listBox2.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBox2ListboxDclick, id=wxID_DIALOGANNLISTBOX2)
    self.listBox2.Bind(wx.EVT_KEY_DOWN, self.OnListBox2KeyDown)
    self.listBox2.Bind(wx.EVT_CHAR, self.OnListBox2Char)

    self.staticText1 = wx.StaticText(id=wxID_DIALOGANNSTATICTEXT1, label='Trays', name='staticText1', parent=self.panel3, pos=wx.Point(3, 3),
      size=wx.Size(170, 13), style=0)

    self.staticText2 = wx.StaticText(id=wxID_DIALOGANNSTATICTEXT2, label='Slides', name='staticText2', parent=self.panel3, pos=wx.Point(3, 189),
      size=wx.Size(170, 13), style=0)

    self.staticText3 = wx.StaticText(id=wxID_DIALOGANNSTATICTEXT3, label='Picture', name='staticText3', parent=self.panel4, pos=wx.Point(0, 25),
      size=wx.Size(811, 13), style=0)

    self.panel5 = wx.Panel(id=wxID_DIALOGANNPANEL5, name='panel5', parent=self.panel4, pos=wx.Point(0, 0), size=wx.Size(811, 25),
      style=wx.TAB_TRAVERSAL)

    self.genToggleButton1 = wx.lib.buttons.GenToggleButton(id=wxID_DIALOGANNGENTOGGLEBUTTON1, label='Ellipse', name='genToggleButton1',
      parent=self.panel5, pos=wx.Point(112, 0), size=wx.Size(101, 25), style=0)
    self.genToggleButton1.SetToggle(False)
    self.genToggleButton1.Bind(wx.EVT_BUTTON, self.OnGenToggleButton1Button, id=wxID_DIALOGANNGENTOGGLEBUTTON1)

    self.genToggleButton2 = wx.lib.buttons.GenToggleButton(id=wxID_DIALOGANNGENTOGGLEBUTTON2, label='Rectangle', name='genToggleButton2',
      parent=self.panel5, pos=wx.Point(213, 0), size=wx.Size(101, 25), style=0)
    self.genToggleButton2.SetToggle(False)
    self.genToggleButton2.Bind(wx.EVT_BUTTON, self.OnGenToggleButton2Button, id=wxID_DIALOGANNGENTOGGLEBUTTON2)

    self.staticText4 = wx.StaticText(id=wxID_DIALOGANNSTATICTEXT4, label='Samples/colonies', name='staticText4', parent=self.panel3, pos=wx.Point(3,
      491), size=wx.Size(170, 13), style=0)

    self.listBox3 = wx.ListBox(choices=[], id=wxID_DIALOGANNLISTBOX3, name='listBox3', parent=self.panel3, pos=wx.Point(0, 507), size=wx.Size(176,
      167), style=0)
    self.listBox3.Bind(wx.EVT_LISTBOX, self.OnListBox3Listbox, id=wxID_DIALOGANNLISTBOX3)
    self.listBox3.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListBox3ListboxDclick, id=wxID_DIALOGANNLISTBOX3)
    self.listBox3.Bind(wx.EVT_KEY_DOWN, self.OnListBox3KeyDown)
    self.listBox3.Bind(wx.EVT_CHAR, self.OnListBox3Char)

    self.button1 = wx.Button(id=wxID_DIALOGANNBUTTON1, label='Change picture', name='button1', parent=self.panel5, pos=wx.Point(0, 0),
      size=wx.Size(112, 25), style=0)
    self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button, id=wxID_DIALOGANNBUTTON1)

    self.panelPictureFrame = wx.Panel(id=wxID_DIALOGANNPANELPICTUREFRAME, name='panelPictureFrame', parent=self.panel4, pos=wx.Point(0, 38),
      size=wx.Size(811, 637), style=wx.TAB_TRAVERSAL)
    self.panelPictureFrame.SetBackgroundColour(wx.Colour(0, 0, 0))
    self.panelPictureFrame.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)

    self._init_sizers()

  def init_panelPicture(self, prnt):
    
    def OnCanvasKeyDown(event):
      self.process_key_event(event)


    self.panelPictureFrame.Bind(wx.EVT_KEY_DOWN, OnCanvasKeyDown)
      
    #self.panelPicture = fc.FloatCanvas(id=wxID_DIALOGANNPANELPICTURE, name='panelPicture', parent=self.panelPictureFrame, pos=wx.Point(1, 1),
    #  size=wx.Size(452, 411))
    
    #self.panelPicture = fc.FloatCanvas(id=wxID_DIALOGANNPANELPICTURE, parent=self.panelPictureFrame)
    self.panelPicture = nc.NavCanvas(id=wxID_DIALOGANNPANELPICTURE, parent=self.panelPictureFrame)
    self.panelPicture.Bind(wx.EVT_KEY_DOWN, OnCanvasKeyDown)
    self.canvas = self.panelPicture.Canvas
    self.canvas.Bind(wx.EVT_KEY_DOWN, OnCanvasKeyDown)

    #self.panelPicture = wx.Panel(id=wxID_DIALOGANNPANELPICTURE, parent=self.panelPictureFrame)

    #self.canvas.Bind(wx.EVT_LEFT_DOWN, self.OnPanelPictureLeftDown)
    #self.canvas.Bind(wx.EVT_LEFT_UP, self.OnPanelPictureLeftUp)
    self.canvas.Bind(wx.EVT_MOTION, self.OnPanelPictureMotion)

    self.boxSizer6.AddWindow(self.panelPicture, 1, border=1, flag=wx.ALL | wx.GROW)

    self.panelPictureFrame.Layout()

  def __init__(self, parent):
    self._init_ctrls(parent)
    self.init_panelPicture(parent)
    self.fill_listbox1()
   
  ############################################################################################################
  ## Tools
  
  def OnButton1Button(self, event):
    try:
      if self.what_ann == ANN_NOTHING:
        raise error_x("No tray or slide selected.")
        
      dlg = wx.FileDialog(self, 'Choose an image file', t_setup.get_value("path_image"), '', '*.*', wx.OPEN)
      try:
        if dlg.ShowModal() == wx.ID_OK:
          filename = dlg.GetPath()
          
          t_setup.update({"path_image": os.path.dirname(filename)})


          if self.what_ann == ANN_TRAY:          
            t_tray.import_picture(filename, self.idtray)
            self.change_tray(self.idtray)
          else:
            t_slide.import_picture(filename, self.idslide)
            self.change_slide(self.idslide)

          
      finally:
        dlg.Destroy()
    except error_x, e:
      import act_main
      act_main.handle_exception(e)

  
  def sync_tool_buttons(self):
    """Puts only one tool button down and the others up according to the selected tool (self.what_tool)."""
    data = ((TOOL_ELLIPSE, self.genToggleButton1), (TOOL_RECTANGLE, self.genToggleButton2))
    for (tool, object) in data:
      object.SetValue(tool == self.what_tool)


  def OnGenToggleButton1Button(self, event):
    # Registers what tool to be used but actual drawing depends on other states
    btn = event.GetEventObject()
    
    self.cancel_action()

    if btn.GetToggle():
      self.what_tool = TOOL_ELLIPSE
    else:
      self.what_tool = TOOL_NONE

    self.sync_tool_buttons()

  def OnGenToggleButton2Button(self, event):
    # Registers what tool to be used but actual drawing depends on other states
    btn = event.GetEventObject()

    self.cancel_action()

    if btn.GetToggle():
      self.what_tool = TOOL_RECTANGLE
    else:
      self.what_tool = TOOL_NONE
    self.sync_tool_buttons()


  ##################################################################################
  ### Events in listbox
  
  def do_dclick_listbox1(self):
    #This event is called when the user selects a tray
    index = self.listBox1.GetSelection()

    _idtray = self.data_tray[index][0]
    #if self.idtray <> _idtray:
    self.change_tray(_idtray)

  def do_dclick_listbox2(self):
    index = self.listBox2.GetSelection()
    
    _idslide = self.data_slide[index][0]
    #if self.idslide <> _idslide:
    self.change_slide(_idslide)

  def do_dclick_listbox3(self):
    if self.what_ann == ANN_SLIDE:
      index = self.listBox3.GetSelection()
      if index > -1:
        self.call_chart(index)
  
   
  def OnListBox1Listbox(self, event):
    event.Skip()

  def OnListBox1ListboxDclick(self, event):
    self.do_dclick_listbox1()

  def OnListBox2Listbox(self, event):
    if self.what_ann == ANN_TRAY:
      index = self.listBox2.GetSelection()
      if index > -1:
        self.change_index(index)

  def OnListBox2ListboxDclick(self, event):
    self.do_dclick_listbox2()
    

  def OnListBox3Listbox(self, event):
    if self.what_ann == ANN_SLIDE:
      index = self.listBox3.GetSelection()
      if index > -1:
        self.change_index(index)

  def OnListBox3ListboxDclick(self, event):
    self.do_dclick_listbox3()


  ###################################################################
  ## Events in canvas
  
  def OnPictureLeftDown(self, picture):
    if self.what_tool <> TOOL_NONE and self.pairs:
      coords = picture.HitCoords #self.get_hit_coords(picture)
        
      if self.what_action == ACTION_NONE:
        self.create_object(coords, self.pairs.caption)

      elif self.what_action == ACTION_SELECTED:
        self.cancel_selected()
        self.create_object(coords, self.pairs.caption)
    else:
      print "Not ready to draw"
      
    #event.Skip()

  def OnPictureLeftUp(self, picture):
    if self.what_action == ACTION_DEFINING:
      coords = picture.HitCoords
      
      THRESHOLD = 13
      
      if abs(coords[0]-self.coords_ini[0]) < THRESHOLD or abs(coords[1]-self.coords_ini[1]) < THRESHOLD:
        self.cancel_defining()
      else:
        self.confirm_defining()


  def OnPanelPictureMotion(self, event):
    if self.what_action == ACTION_NONE:
      pass
    else:
      coords = self.get_canvas_coords(event)
    
      if self.what_action == ACTION_DEFINING:
        self.resize_shape(self.coords_ini, (coords[0]-self.coords_ini[0], coords[1]-self.coords_ini[1]))

  def OnDialogAnnClose(self, event):
    self.save()
    event.Skip()

  def OnListBox1KeyDown(self, event):
    key = event.GetKeyCode()
    if event.ControlDown() and key == ord('L'):
      self.do_dclick_listbox1()
    else:
      event.Skip()
        

  def OnListBox2KeyDown(self, event):
    key = event.GetKeyCode()
    if event.ControlDown() and key == ord('L'):
      self.do_dclick_listbox2()
    else:
      event.Skip()

  def OnListBox3KeyDown(self, event):
    key = event.GetKeyCode()
    if event.ControlDown() and key == ord('L'):
      self.do_dclick_listbox3()
    else:
      event.Skip()

  def OnListBox1Char(self, event):
    event.Skip()

  def OnListBox2Char(self, event):
    event.Skip()

  def OnListBox3Char(self, event):
    event.Skip()




