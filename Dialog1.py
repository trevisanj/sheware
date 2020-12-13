#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1] = [wx.NewId() for _init_ctrls in range(1)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        wx.Dialog.__init__(self, style=wx.DEFAULT_DIALOG_STYLE, name='', parent=prnt, title='Dialog1', pos=wx.Point(-1, -1), id=wxID_DIALOG1, size=wx.Size(-1, -1))

    def __init__(self, parent):
        self._init_ctrls(parent)
