import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

phi, I = np.genfromtxt('data_scripts/data/polarisation.txt', unpack = True)

phi = np.deg2rad(phi)

def f(phi, I0, a, phi0, b):
    return I0 * (np.cos(a*phi + phi0))**2 + b

params, covariance_matrix = curve_fit(f, phi, I)

uncertainties = np.sqrt(np.diag(covariance_matrix))

phi_plot = np.linspace(phi[0], phi[-1], 1000)

plt.xlabel(r'$\varphi \mathbin{/} \si{\radian}$')
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], [r'$0$', r'$\pi /2$', r'$\pi$', r'$\frac{3}{2}\pi$', r'$2\pi$'])
plt.xlim(-0.2, 2*np.pi)
plt.ylabel(r'$I \mathbin{/} \si{\milli\watt}$')
plt.plot(phi, I,'.', label = 'Messwerte')
plt.plot(phi_plot, f(phi_plot, *params), "-", label='Fit')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/polarisation.pdf')

 
paramsname = np.array(['I0', 'a', 'phi0', 'c'])

ab = np.zeros(paramsname.size, dtype=[('paramsname', 'U6'), ('params_values', float), ('uncertainties', float)])
ab['paramsname'] = paramsname
ab['params_values'] = params
ab['uncertainties'] = uncertainties
np.savetxt(
    'data_scripts/data/fitparameter_polarisation.txt',
    ab,
    fmt="%10s , %10.3f, %10.3f",
    delimiter=',',
    header='paramsname, params, uncertainties',
) 