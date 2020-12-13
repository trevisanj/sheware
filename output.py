"""Output module. To implement new output behavior please replace the output attribute"""
import wx

OUTPUT_ERROR = 0
OUTPUT_WARNING = 1
OUTPUT_INFO = 2

LEGEND = {OUTPUT_ERROR: "*ERROR* ", OUTPUT_WARNING: "-Warning- ", OUTPUT_INFO: ""}

ctrl = None # wx.TextCtrl used for log output
ctrl2 = None


def progress_handler(perc):
  output_handler("- %5.1f %% -" % (perc*100,))

def output_handler(s, severity = 2, flag_messagebox = False):
  if ctrl or ctrl2:
    ss = LEGEND[severity]+str(s)+"\n"
    if ctrl:
      ctrl.AppendText(ss)
    if ctrl2:
      ctrl2.AppendText(ss)
      
    if flag_messagebox:
      if severity == OUTPUT_INFO:
        wx.MessageBox(str(s), "Information", wx.OK | wx.ICON_INFORMATION, None)
      elif severity == OUTPUT_WARNING:
        wx.MessageBox(str(s), "Warning", wx.OK | wx.ICON_WARNING, None)
      elif severity == OUTPUT_ERROR:
        wx.MessageBox(str(s), "Error", wx.OK | wx.ICON_ERROR, None)
  else:
    print LEGEND[severity]+s



output = output_handler
progress = progress_handler