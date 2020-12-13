import file_importer_pirouette_dat
import file_importer_csv

def get_tuple():
  """Returns a tuple ((name, class object), ..."""
  return ((file_importer_pirouette_dat.name, file_importer_pirouette_dat.file_importer_pirouette_dat), 
          (file_importer_csv.name, file_importer_csv.file_importer_csv), 
         )