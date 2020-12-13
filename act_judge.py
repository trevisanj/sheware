"""These are the actions primary related to DialogJudge, but any module can use them. Basically it provides ways for visually inserting, editting and
updating the db:judge table."""
import output
import wx
import session
from errors import *
import DialogEditJudge
from table_judge import t_judge
from judge import *
from judge_score import *
import glob
import os.path

  
def insert():
  """Calls the edit dialog in insert mode. Returns True of False whether a record has been inserted or not."""
  result = False
  dlg = DialogEditJudge.create(None)
  dlg.set_mode("insert")
  try:
    dlg.ShowModal()
    if dlg.result == wx.ID_OK:
      result = True
    else:
      raise error_abort("Insert canceled.")
  finally:
    dlg.Destroy()
  return result


def edit(id):
  """Calls the edit dialog in edit mode. Returns True of False whether a record has been edited or not."""
  result = False
  dlg = DialogEditJudge.create(None)
  dlg.set_mode("edit")
  dlg.set_id(id)
  try:
    dlg.ShowModal()
    if dlg.result == wx.ID_OK:
      result = True
    else:
      raise error_abort("Edit canceled.")
  finally:
    dlg.Destroy()
  return result

def delete(id):
  if wx.MessageBox("Are you sure, mate?", "Confirm delete", wx.YES_NO, None) == wx.YES:
    # raise error_x("Sorry, this action is too dangerous to be performed!")
    t_judge.delete(id)
  else:
    raise error_abort("Delete not confirmed.")

def get_judge_classes():
  """Returns a [(class_name, description), ...]"""
  """Tests judge code introspection"""


  ll = []
  files = glob.glob('./judge_*.py')
  for file in [os.path.basename(fil_) for fil_ in files]:
    class_name = file[0:file.find('.')]
    
    jg = judge_object(class_name)
    ll.append((class_name, jg.get_description(), isinstance(jg, judge_score)))
  
    # I can implement a jg.flag_selectable if needed
    
  return ll
