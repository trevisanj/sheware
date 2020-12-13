"""CSV file import routine.
Note that it considers that all data in CSV file belong to the same colony.
"""

name = "CSV"

import file_importer
import fileinput
import os.path
from table_tray import t_tray
from table_slide import t_slide
from table_colony import t_colony
from table_spectrum import t_spectrum
from table_series import t_series
from output import *
from errors import *
import re


class file_importer_csv(file_importer.file_importer):
  
#  def parse_colony_code(self, colony_code):
#    file_importer.parse_colony_code(self)
#    self.colony_code += "_"+str(self.lineno)
    

  def import_file_(self):
    self.import_file__(False)

  def simulate_(self):
    self.import_file__(True)
  
  def import_file__(self, flag_simulate):
    colony_code = os.path.basename(self.file_name)
    self.parse_colony_code(colony_code)
    output("Colony code: '%s'." % self.colony_code)
    
    import csv
    o_reader = csv.reader(self.file_handle)
    
    self.lineno = 0
    for s_y_s in o_reader:
      wncount = len(s_y_s)
      if self.lineno == 0:
        output("Wavenumber count: %s" % wncount)

      self.assure_good_wncount(wncount)
      
      if not flag_simulate:
        self.create_spectrum()

      y_values = [float(s) for s in s_y_s]
        
      if not flag_simulate:
        for s_y in y_values:
          t_series.insert(self.idspectrum, self.idexperiment, s_y)
        self.count_series += 1
        
      self.lineno += 1
      
    
    
    