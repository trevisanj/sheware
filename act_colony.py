"""These are the actions primary related to DialogColony, but any module can use them. Basically it provides ways for visually inserting, editting and
updating the db:Colony table."""
import output
import wx
import session
from errors import *
import DialogEditColony
from table_colony import t_colony

  
def insert(idslide):
  """Calls the edit dialog in insert mode. Returns True of False whether a record has been inserted or not."""
  result = False
  dlg = DialogEditColony.create(None)
  dlg.idslide = idslide
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
  dlg = DialogEditColony.create(None)
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
    t_colony.delete(id)
  else:
    raise error_abort("Delete not confirmed.")

