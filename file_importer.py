import fileinput
import re
from output import *
from db_con import con
from table_tray import t_tray
from table_slide import t_slide
from table_colony import t_colony
from table_spectrum import t_spectrum
from table_series import t_series
from table_experiment import t_experiment
from table_domain import t_domain
from errors import *
from session import session
import os.path

class file_importer(object):
  """File importer. This class does not import any file (import_file_() is abstract, but provides all structure for
     a descending class."""
  
  __idexperiment = -1
  __iddomain = -1
  __wncount = -1
  file_name = None

  # Default values  
  __regexp_file_name = "^([A-Z]{1,4})([0-9]+)([A-Z])"
  pattern_tray = "%(0)s"
  pattern_slide = "%(0)s%(1)s"
  pattern_colony = "%(0)s%(1)s%(2)s"  
  slide_digits = 0

  p_file_name = None # Compiled regexp which corresponds to __regexp_file_name
  flag_re_compiled = False
  
  count_tray = 0
  count_slide = 0
  count_colony = 0
  count_spectrum = 0
  count_spectrum_replaced = 0
  count_series = 0
  count_series_replaced = 0
  
  flag_forreal = True # In case this is false, all routines MUSTN'T CHANGE THE DATABASE!!!!!!!!
  
  def __init__(self):
    self.id_bank = []
    self.colony_keys = []
    self.slide_keys = []
    self.tray_keys = []
    self.colony_ids = []
    self.slide_ids = []
    self.tray_ids = []
    
      
    #compiles all regexp patterns to be used later
    self.p_dec = re.compile("\d+")
    self.p_eol = re.compile("[\r\n]");
    self.p_alpha = re.compile("[a-zA-Z]+")

  def set_idexperiment(self, value):
    self.__idexperiment = value

  def set_iddomain(self, value):
    self.__wncount = t_domain.get_value_from_id("wncount", value)
    output("* Current wncount: %d" % self.__wncount)
    self.__iddomain = value


  idexperiment = property(fget=lambda(self): self.__idexperiment, fset=set_idexperiment)
  iddomain = property(fget=lambda(self): self.__iddomain, fset=set_iddomain)
  wncount = property(fget=lambda(self): self.__wncount)
  
  def set_regexp_file_name(self, value): 
    self.__regexp_file_name = value
  
  regexp_file_name = property(fget=lambda(self): self.__regexp_file_name, fset=set_regexp_file_name)
  
  def assure_ready(self):
    """Checks if the object is properly set for file import"""
    if (self.file_name == None):
      raise error_x("Must provide a file name.")
    if (self.idexperiment <= 0):
      raise error_x("idexperiment is not defined.")
    if (self.iddomain <= 0):
      raise error_x("iddomain is not defined.")
    
    self.assure_re_compiled()

  def assure_re_compiled(self):    
    if not self.flag_re_compiled:
      self.p_file_name = re.compile(self.__regexp_file_name)
      flag_re_compiled = True

    
  def assure_good_wncount(self, wncount):
    """Compares wavenumber count to previous spectra.
    
    If self.wncount is -1, this probably means that the experiment has no spectrum yet. Then, @wncount will be assumed as correct and
    (self.wncount and cells.domain.wncount) will be updated.
    
    If self.wncount is not -1, this routine compares it to @wncount and they must be the same, otherwise an exception will be raised."""

    if self.wncount > -1:
      if wncount <> self.wncount:
        raise error_x("File '%s' has invalid data length: %s (should be %s)" % (self.file_name, wncount, self.wncount))
    else:
      self.__wncount = wncount
      if self.flag_forreal:
        print "EEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAAAA PRAAAAAAAAAAAAAAAAAAAAA"
        print "iddomain: "+str(self.iddomain)+"; wncount ---------------> "+str(wncount)
        t_domain.update({"wncount": wncount}, self.iddomain)
        
        raise error_x("OUT OF HERE!!!!!!!!!")
        
    
  def import_file(self):
    self.assure_ready()

    output("")
    output("----- File: %s ------" % self.file_name)
    
    try:
      self.file_handle = fileinput.input(self.file_name)
      self.lineno = 0
      self.import_file_()
    except error_x, e:
      output("line "+(self.lineno+1).__str__()+": "+e.message, OUTPUT_ERROR)
      raise
    finally:
      if self.file_handle != None:
        self.file_handle.close()

  def import_file_(self):
    raise error_x("file_importer.import_file_() must be inherited!")
  
  

#  def simulate(self):
#    self.assure_ready()
#
#    output("* Simulating file "+self.file_name)
#    
#    try:
#      self.file_handle = fileinput.input(self.file_name)
#      self.lineno = 0
#      self.count_series = 0
#      self.simulate_()
#    except error_x, e:
#      output(e.message)
#      raise
#    finally:
#      output("# inserted into series: %d" % self.count_series)
#      if self.file_handle != None:
#        self.file_handle.close()
#
#  def simulate_(self):
#    """Most common procedure for determining tray, slide and colony codes is taking them from file name. Therefore, the default procedure is implemented in file_import."""
#
#    colony_code = os.path.basename(self.file_name)
#    self.parse_colony_code(colony_code)
#    
#    output("Tray: '%s' ; Slide: '%s' ; Colony: '%s'" % (self.tray_code, self.slide_code, self.colony_code))
  

  def parse_colony_code(self, colony_code):
    """This method returns (tray_code, tray_code+slide_code)
    
    Sample code is <tray_code><slide_code><colony_code>
    <tray_code> is all letters
    <slide_code> is all numbers
    [<colony_code>] is all letters
    
    Ex: UX32A"""

    self.assure_re_compiled()

    if len(colony_code) > 99:
      raise error_x("Colony code cannot have more than 99 characters: '%s'." % colony_code)
    
    s = colony_code.upper()
    
    o = re.search(self.p_file_name, s)
    
    if o == None:
      raise error_x("Sample code invalid: %s" % colony_code)
    
    # Mounts a dictionary containing the file_name pieces mathed by the p_file_name regexp. The dictionary is needed to further
    # substitution using strings pattern_*
    pieces = {}
    i = 0
    for piece in o.groups():
      pieces[str(i)] = piece
      i += 1
    
    self.tray_code = self.pattern_tray % pieces
    
    # Slide code may be right-justified with zeros. This will be done if self.slide_digits > 0
    self.slide_code = (self.pattern_slide % pieces)
    if self.slide_digits > 0:
      self.slide_code = self.slide_code.rjust(self.slide_digits, "0")
    
    self.colony_code = self.pattern_colony % pieces
    
    output("Parsed: Tray: '%s' ; Slide: '%s' ; Colony: '%s'" % (self.tray_code, self.slide_code, self.colony_code))


  def write_spectrum(self, y):
    try:
      x = self.tray_code+self.slide_code+self.colony_code
      i = self.colony_keys.index(x)
      self.idtray = self.id_bank[i][0]
      self.idslide = self.id_bank[i][1]
      self.idcolony = self.id_bank[i][2]
    except ValueError:
      try:
        i = self.tray_keys.index(self.tray_code)
        self.idtray = self.tray_ids[i]
      except ValueError:
        print "$$$$$ colony code "+str(self.colony_code)+" nao existe"
      
        (flag, self.idtray) = t_tray.assure(self.tray_code, self.idexperiment, not self.flag_forreal)
        print "$$$$$ tray eh "+str(self.idtray)
        
        
        if flag:
          self.count_tray += 1
        self.tray_keys.append(self.tray_code)
        self.tray_ids.append(self.idtray)

          

      x = self.tray_code+self.slide_code
      try:
        i = self.slide_keys.index(x)
        self.idslide = self.slide_ids[i]
      except:
        (flag, self.idslide) = t_slide.assure(self.slide_code, self.idtray, not self.flag_forreal)
        print "$$$$$ slide eh "+str(self.idslide)
        if flag:
          self.count_slide += 1
        self.slide_keys.append(x)
        self.slide_ids.append(self.idslide)

      (flag, self.idcolony) = t_colony.assure(self.colony_code, self.idslide, not self.flag_forreal)
      print "$$$$$ colony eh "+str(self.idcolony)

      if flag:
        self.count_colony += 1
      
      x = self.tray_code+self.slide_code+self.colony_code
      self.colony_keys.append(x)
      self.id_bank.append((self.idtray, self.idslide, self.idcolony))
      
    # Writes spectrum data
    (flag_new_spectrum, self.idspectrum) = t_spectrum.reset(file_name=os.path.basename(self.file_name), 
    idexperiment=self.idexperiment, iddomain=self.iddomain, idcolony=self.idcolony, flag_simulation = not self.flag_forreal)

    # Writes series data
    (flag_new_series, self.idseries) = t_series.reset(idexperiment=self.idexperiment, 
    iddomain=self.iddomain, idspectrum=self.idspectrum,
    vector=y,
    flag_simulation=not self.flag_forreal)

    # Updates counters
    if flag_new_spectrum:
      self.count_spectrum += 1
    else:
      self.count_spectrum_replaced += 1
    if flag_new_series:
      self.count_series += 1
    else:
      self.count_series_replaced += 1


    print "count_new_series: %d" % self.count_series


def import_many_files(o, path, cards):
  """o is a file_importer instance."""
  import os
  import fnmatch
  all_in_dir = os.listdir(path)
  those = fnmatch.filter(all_in_dir, cards)
  those.sort()
  output("# of files: "+len(those).__str__())
  
  no_imported = 0
  no_errors = 0
  for file_name in those:
    try:
      o.file_name = os.path.join(path, file_name)
      o.import_file()
      no_imported += 1
    except error_x, e:
      output("File import failed: "+e.message, OUTPUT_ERROR)
      no_errors += 1
      #raise
  
  output("# imported: %s" % no_imported)
  output("# errors: %s" % no_errors)
  
  
def ask_and_import_many_files(file_importer_class):
  """Asks for path and filenames (with wildcards) and calls import_many_files()
  
  This routine currently does not work because import_many_files has been updated.
  
  """

  from table_experiment import t_experiment

  s_idexperiment = raw_input("Experiment id: ");
  if len(s_idexperiment) > 0:
    idexperiment = int(s_idexperiment)
    output("(name: '"+t_experiment.get_name_from_id(idexperiment)+"')")
    
    path = raw_input("Please enter path: ");
    if len(path) > 0:
      cards = raw_input("Please enter file names (use wildcards): ");
      if len(cards) > 0:
        import_many_files(file_importer_class, idexperiment, path, cards)


