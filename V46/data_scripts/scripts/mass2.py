import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

wavelength, theta1w1, theta1m1, theta2w1, theta2m1 = np.genfromtxt('data_scripts/data/probe1.txt', unpack = True)
wavelength, theta1w2, theta1m2, theta2w2, theta2m2 = np.genfromtxt('data_scripts/data/probe2.txt', unpack = True)
wavelength, theta1w3, theta1m3, theta2w3, theta2m3 = np.genfromtxt('data_scripts/data/probe3.txt', unpack = True)

wavelength = wavelength

deltatheta1 = np.deg2rad(abs(theta2w1 + theta2m1/60 - theta1w1 - theta1m1/60)/2)
deltatheta2 = np.deg2rad(abs(theta2w2 + theta2m2/60 - theta1w2 - theta1m2/60)/2)
deltatheta3 = np.deg2rad(abs(theta2w3 + theta2m3/60 - theta1w3 - theta1m3/60)/2)

deltathetanorm =    deltatheta3/(1.36e-3)- deltatheta1/(5.11e-3)

deltathetanorm =    np.delete(deltathetanorm, 0)

wavelength = np.delete(wavelength, 0)

def f(wave,a,b):
    return  a*wave**2+ b


params, covariance_matrix = curve_fit(f, wavelength, deltathetanorm)

uncertainties = np.sqrt(np.diag(covariance_matrix))


plt.xlabel(r'$\lambda^2 \mathbin{/} \si{\micro\meter\squared}$')
plt.ylabel(r'$\theta_\text{frei} \mathbin{/} \si{\radian\per\meter}$')

wave_plot = np.linspace(wavelength[0], wavelength[-1], 1000)

print(f'mass2 a = {params[0]} pm {uncertainties[0]} ')
print(f'mass2 b = {params[1]} pm {uncertainties[1]} ')
plt.plot(wavelength**2, deltathetanorm, 'x')
plt.plot(wave_plot**2, f(wave_plot, *params), label = 'Fit')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/mass2.pdf')

