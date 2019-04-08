#=============================================================================#
#
# Performs a linear regression on columns in a single container
#
# are the columns all going to be pd.Series? multiple linear regression
#
#=============================================================================#

import math

import pandas as pd

from .. import container 



def test():

    ...


def _mean(data = None):
    '''
    calculates the mean
    '''
    n = len(data)
    total = sum(data)
    return float(total) / float(n)


def _variance(data = None):
    '''
    variance
    '''
    mean = _mean(data)

    total = 0.0
    for item in data:
        item = float(item)
        diff = item - mean
        total += pow(diff, 2)

    return total / float(len(data) - 1)


def _covariance(data1 = None, data2 = None):
    '''
    covariance
    '''
    mean1 = _mean(data1)
    mean2 = _mean(data2)

    n = min(len(data1), len(data2))

    cov = 0.0
    for i in range(n):
        cov += (data1[i] - mean1) * (data2[i] - mean2)

    return cov / float(n - 1)


def _linear_regression(container, x_col = "", y_col = ""):
    '''
    '''
    x = container[x_col]
    y = container[y_col]

    m = _covariance(x, y) / _variance(x)
    b = _mean(y) - m * _mean(x)

    return m, b


def _multiple_lin_reg(**kwargs):
    '''
    kwargs should be a dictionary of y1 x1, x2, x3...
    '''
    if not isinstance(kwargs, dict):
        return

    pass


def _nonlinear_regression():

    pass


def _polynomial_regression():

    pass


def _logistic_regression():

    pass


def regression():

    pass














