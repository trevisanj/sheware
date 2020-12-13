"""Test for PCA"""

from session import session
from db_con import con

import db_con_setup
db_con_setup.setup()
con.connect()

session.idexperiment = 3

from spectrum_lot import spectrum_lot
from pca_lot import pca_lot

o1 = spectrum_lot()
o1.idexperiment = session.idexperiment
o1.iddomain = session.iddomain
o1.read()

o2 = pca_lot()
o2.spectrum_lot = o1
o2.calculate()