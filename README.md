# wrapODR
This is a simple wrapper around the scipy.odr library (orthogonal distance regression).

## Installation
This package is pip installable using:
`pip install -i https://test.pypi.org/simple/ wrapODR-pjh6654==0.0.3`

## Usage
Below is test code using wrapODR to fit a sigmoid with uncertainies in x and y.

```python
import numpy as np
import matplotlib.pyplot as plt
from wrapODR import labfit as lf

# Random seed
np.random.seed(1)


def g(B, x):
    return B[0] / (1 + np.exp(-(x - B[1])))


#
# Test Parameters
#
n = 20  # number of data points
a = 5.0
b = 0.0
sigma_x = 0.2  # uncertainty in x
sigma_y = 0.2  # uncertainty in y
xmin = -10.0
xmax = 10.0
xarray = np.linspace(xmin, xmax, n)

# generate data
x = np.copy(xarray) + np.random.normal(0.0, sigma_x, n)
y = g([a, b], xarray) + np.random.normal(0.0, sigma_y, n)

# initial guess for fitting
beta0 = [6, 1]

# fit using both x and y uncertainty
params, error, bestfit, chi_vals = lf.fit(g, x, y, sigma_x, sigma_y, beta0=beta0)

# Plot and print results of the fit
print("B[0] = {:.3f} +/- {:.3f}".format(params[0], error[0]))
print("B[1] = {:.3f} +/- {:.3f}".format(params[1], error[1]))
print("Chi-Squared: {:.3f}".format(chi_vals[0]))
print("Reduced Chi-Squared: {:.3f}".format(chi_vals[1]))
plt.errorbar(x, y, xerr=sigma_x, yerr=sigma_y, fmt='.', capsize=3)
plt.plot(*bestfit)
plt.show()
```

