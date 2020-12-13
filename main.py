#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frame_main

modules ={u'frame_main': [1, 'Main frame of Application', u'frame_main.py'],
 u'frame_table': [0, '', u'frame_table.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frame_main.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
