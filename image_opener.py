import wx
from output import output

class image_opener(object):
  def __init__(self, file_name=None, max_pixels=786432):
    self.file_name = file_name
    self.max_pixels = max_pixels
    
  def __read(self):
    """Reads file, scales image if necessary and stores it in internal image object."""
    
    img = wx.Image(self.file_name, wx.BITMAP_TYPE_ANY)
    
    iwidth, iheight = img.GetWidth(), img.GetHeight()
    ipixels = iwidth*iheight
    
    if ipixels > self.max_pixels:
      # Image is too big, needs rescale
      pixel_ratio = float(self.max_pixels)/ipixels
      factor = pixel_ratio**(1./2)
      
      newwidth = int(iwidth*factor)
      newheight = int(iheight*factor)

      img = img.Rescale(newwidth, newheight)

      output("Had to rescale file %s: (%d, %d) --> (%d, %d)." % (self.file_name, iwidth, iheight, newwidth, newheight))
    
    self.__img = img
    
    
  def to_string(self):
    """Reads file, scales image if necessary and returns binary string. Image is converted to PNG."""
    
    self.__read()
    
    import cStringIO
    h = cStringIO.StringIO()
    
    self.__img.SaveStream(h, wx.BITMAP_TYPE_JPEG) 

    s = h.getvalue()
    
    output("Stream from file %s has %d bytes." % (self.file_name, len(s)))
    
    return s
    