#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import frame_main
import sys
sys.path.append('setup')


modules ={u'frame_main': [1, 'Main frame of Application', u'frame_main.py'],
 u'frame_table': [0, '', u'frame_table.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frame_main.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
      
    


def redirect_output_handler(frame):
  from act_main import setup_output_handler
  setup_output_handler(frame)

def main():
  flag_db = False
  import _mysql
  try:
    import db_con
    db_con.setup()
    db_con.con.connect()
    flag_db = True
  except _mysql.OperationalError, e:
    print 'ERROR: connecting to database: '+str(e.args[1])+'. '
    
    if e.args[0] == 1045:
      print '\nPossible causes:\n  The file \'setup/database.py\' is wrong\n  The database server is wrong'


  if flag_db:
    application = BoaApp(0)
    
    # Output will be main frame green over black textbox
    import output
    output.ctrl = application.main.textCtrlLog
  
    from table_setup import t_setup
    
    import act_main
    from session import session
    #session.idexperiment = 3  # This is only for convenience and should be taken off
    act_main.select_experiment()
    #act_main.report_maps()
    #act_main.file_import()
    
    application.MainLoop()

if __name__ == '__main__':
    
    main()
