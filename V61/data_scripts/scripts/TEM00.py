import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, I = np.genfromtxt('data_scripts/data/TEM00.txt', unpack = True)

def f(x, I0, x0, w):
    return I0 * np.exp(-(x-x0)**2/(2*w**2))

params, covariance_matrix = curve_fit(f, x, I)

uncertainties = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(x[0], x[-1], 1000)

plt.xlabel(r'$x \mathbin{/} \si{\milli\meter}$')
plt.ylabel(r'$I \mathbin{/} \si{\milli\watt}$')
plt.plot(x, I,'.', label = 'Messwerte')
plt.plot(x_plot, f(x_plot, *params), "-", label='Fit')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/TEM00.pdf')


paramsname = np.array(['I0', 'x0', 'w^2'])
ab = np.zeros(paramsname.size, dtype=[('paramsname', 'U6'), ('params_values', float), ('uncertainties', float)])
ab['paramsname'] = paramsname
ab['params_values'] = params
ab['uncertainties'] = uncertainties
 

np.savetxt( 
    'data_scripts/data/fitparameter_TEM00.txt',
    ab,
    fmt="%10s , %10.3f, %10.3f",       # first column integer, second 4 digits float
    delimiter=',',
    header='paramsname, params, uncertainties',
)

