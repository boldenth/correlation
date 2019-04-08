"""



correlation imports

"""

#=============================================================================#
# 
# 
# 
#=============================================================================#

__version__ = "0.3"



import numpy
import pandas
import scipy
import sklearn
#import matplotlib.pyplot as plt

from correlation.container import Container

from correlation.io.converter import \
     convert_file, \
     convert_time

from correlation.io.conversions import \
     _si_time, \
     _si_len

from correlation.analysis.api import \
     linear_regression, \
     MakeDecision

