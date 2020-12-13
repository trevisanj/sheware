"""Tests judge code introspection"""

from judge import *
import glob
import os.path

files = glob.glob('./judge_*.py')

for file in [os.path.basename(fil_) for fil_ in files]:
  class_name = file[0:file.find('.')]
  
  jg = judge_object(class_name)
  print jg
  
  # I can implement a jg.flag_selectable if needed
