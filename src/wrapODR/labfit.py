# Author: Peter Hart <pjh6654@rit.edu>

import sys
import numpy as np
from scipy.odr import ODR, Model, RealData


def _chi_values(f, x, y, yerr, params):
    # First we need to check if error for the dependent variable is given.
    # These errors are necessary for calculating chi-squared values.
    # If errors are not given the chi and red_chi values set to None.
    if yerr is not None:
        chi = np.sum(((y - f(params, x)) / yerr) ** 2)
        red_chi = chi / (len(x) - len(params))
    else:
        print("There is no y error to calculate chi-squared values!\n"
              "Chi-squared values returned as None.", file=sys.stderr)
        chi = red_chi = None
    return [chi, red_chi]


def fit(f, xdata, ydata, xerr=None, yerr=None, beta0=None, bf_res=500, maxit=50):
    """
    Fits a general function f(params, x) to data (xdata, ydata),
    accounting for uncertainties in both the independent and dependent
    variables.

    Parameters
    ----------
    f:
        Function of the form f(param, x), where param is an array of size M
        and x is an array containing values of the independent variable.
    xdata:
        Array of size N containing independent variable.
    ydata:
        Array of size N containing dependent variable.
    xerr:
        Uncertainty in the independent variable, must be a float or an array of
        size N.
    yerr:
        Uncertainty in the dependent variable, must be a float or an array of
        size N.
    beta0:
        Array of size M containing initial guesses for parameter values.
    bf_res:
        Int defining the number of points in the best fit array.
    maxit:
        Int specifying the maximum number of iterations to perform

    Returns
    -------
    params:
        Array of size M containing parameter estimates.
    param_error:
        Array of size M containing the standard errors of the estimated
        parameters.
    bestfit:
        Array of shape (2, bf_res) containing x and y values for the best fit curve.
    chi_vals:
        List containing chi-squared and reduced chi-squared values respectively
        [chi, red_chi]
    """
    # create the model using the general function and fit the data using scipy.odr
    mod = Model(f)
    data = RealData(xdata, ydata, xerr, yerr)
    result = ODR(data, mod, beta0, maxit=maxit).run()
    # extract the estimated parameters and parameter errors
    params = result.beta
    param_error = result.sd_beta
    # calculate chi-squared and reduced chi-squared values
    chi_vals = _chi_values(f, xdata, ydata, yerr, params)
    # create the best fit array by evaluating f using the estimated parameters
    resx = np.linspace(np.min(xdata), np.max(xdata), bf_res)
    bestfit = [resx, f(params, resx)]

    return params, param_error, bestfit, chi_vals
