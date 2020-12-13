from table_spectrum import t_spectrum
from table_series import t_series
from table_experiment import t_experiment
import numpy as np
import scipy.linalg as la
from output import *
import math

class pca_lot(object):
  
  spectrum_lot = None # spectrum_lot object
  
  __flag_calculated = False
  


  def calculate(self):
    """Calculates self.scores, self.cov and self.eig
    
    self.all_centered: mean-centered spectra (each spectrum centered by its own mean).
    
    self.cov: covariance matrix of self.all_centered
    
    self.eigenvec: eigenvectors of self.cov
    
    self.eigenval: eigenvalues of self.cov

    self.scores: has rows as PC scores. Each score vector contains the coeficients of a linear combination of the eigenvectors of the covariance matrix
                 that recontructs the original spectrum.
                 The score vector is a linear transformation of the original spectrum.

"""

    output("Calculating PCA data...")
    try:
      self.spectra = self.spectrum_lot.all
      spectra = self.spectra
      (no_observations, no_features) = spectra.shape
      
      # Initializes all the "outputs".
      
      
      # calculates the means for each feature. The "axis" is the first one (x/cols/features)
      self.means = spectra.mean(0)
      means = self.means
      
      print "MEANS: ", means

      # Calculates the mean-centered spectra.
      self.all_centered = np.zeros((no_observations, no_features))
      all_centered = self.all_centered
      
      
      for i in range(0, no_features):
        self.all_centered[:, i] = spectra[:, i]-means[i]

      print "ALL_CENTERED: ", all_centered

        
      self.cov = np.dot(all_centered.transpose(), all_centered)/(no_observations-1)

      #print "COV: ", self.cov

      (_eigenvals, _eigenvecs) = la.eig(self.cov)
      
      #print "------------ before ------------"
      #print _eigenvals, _eigenvecs
      
      # This shit doesn't come sorted, so we turn inside out to sort it ourselves.
      temp = []
      for i in range(0, no_features):
        temp.append((_eigenvals[i], np.array(_eigenvecs[:, i])))
        
      
      def compare(a, b):
        n1 = abs(a[0])
        n2 = abs(b[0])
        if n1 > n2:
          return 1
        elif n1 < n2:
          return -1
        return 0
      
      temp.sort(reverse=True, cmp=compare) # Yes, reverse. Remember we want bigger first

      eigenvals = _eigenvals
      self.eigenvals = eigenvals
      eigenvecs = _eigenvecs
      self.eigenvecs = eigenvecs
      
      i = 0
      for (eigenvalue, eigenvector) in temp:
        eigenvals[i] = eigenvalue
        eigenvecs[:, i] = eigenvector
        i += 1
      
      
      # It really doesn't matter if the eigenvectors are layed horizontally or vertically because the eigenvector matrix is symmetric.
      self.scores = np.dot(all_centered, self.eigenvecs)  

    
      output("...done!")
      self.__flag_calculated = True
    except:
      output("...failed!")
      raise


  def assert_calculated(self):
    if not self.__flag_calculated:
      raise error_x("PCA has to be calculated first!", self)
        
  def get_loading(self, wn_index):
    self.assert_calculated()
    
    (no_observations, no_features) = self.spectrum_lot.all.shape
    
    
    #scores_cross = self.all_centered[:, wn_index]
    scores_cross = self.scores[:, wn_index]
    scores_cross_mean = scores_cross.mean()

    scores_cross_centered = scores_cross-scores_cross_mean
    scores_cross_sd = math.sqrt(scores_cross_centered.var(ddof=1))
    
    result = np.zeros(no_features)
    
    for i in range(0, no_features):
      v2 = self.all_centered[:, i]
      v2_sd = math.sqrt(v2.var(ddof=1))
      result[i] = np.dot(scores_cross_centered, v2)/(no_observations-1)/(scores_cross_sd*v2_sd)
      
    return result
    
    
      
      