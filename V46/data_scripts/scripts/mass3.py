import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

wavelength, theta1w1, theta1m1, theta2w1, theta2m1 = np.genfromtxt('data_scripts/data/probe1.txt', unpack = True)
wavelength, theta1w2, theta1m2, theta2w2, theta2m2 = np.genfromtxt('data_scripts/data/probe2.txt', unpack = True)
wavelength, theta1w3, theta1m3, theta2w3, theta2m3 = np.genfromtxt('data_scripts/data/probe3.txt', unpack = True)

wavelength = wavelength*1e-6

deltatheta1 = np.deg2rad(abs(theta2w1 + theta2m1/60 - theta1w1 - theta1m1/60)/2)
deltatheta2 = np.deg2rad(abs(theta2w2 + theta2m2/60 - theta1w2 - theta1m2/60)/2)
deltatheta3 = np.deg2rad(abs(theta2w3 + theta2m3/60 - theta1w3 - theta1m3/60)/2)

deltathetanorm =    deltatheta2/(1.296e-3)- deltatheta1/(5.11e-3)

deltathetanorm =    np.delete(deltathetanorm, 0)

wavelength = np.delete(wavelength, 0)

wavelength2 = wavelength**2 #m^2

params, covariance_matrix = np.polyfit(wavelength2, deltathetanorm, deg = 1, cov = True)

errors = np.sqrt(np.diag(covariance_matrix))

plt.xlabel(r'$\lambda^2 \mathbin{/} \si{\micro\meter\squared}$')
plt.ylabel(r'$\theta_\text{frei} \mathbin{/} \si{\radian\per\meter}$')

wave_plot = np.linspace(wavelength2[0], wavelength2[-1], 1000)

a_err = ufloat(params[0], errors[0])

m = np.sqrt((1.602e-19)**3/(8*(np.pi)**2*8.8541878128e-12*299792458**3)*0.428*2.8e24/3.374 /params[0])

m_err = 0.5 * np.sqrt((1.602e-19)**3/(8*(np.pi)**2*8.8541878128e-12*299792458**3)*0.428*2.8e24/3.374) * 1/params[0]**(3/2) * errors[0]

print(f'mass3 a = {params[0]} pm {errors[0]} ')
print(f'mass3 b = {params[1]} pm {errors[1]} ')
print(f'mass2 m = {m} pm {m_err}')
plt.plot(wavelength2*1e12, deltathetanorm, 'x') #µm
plt.plot(wave_plot*1e12, params[0]*wave_plot + params[1], label = 'Fit')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/mass3.pdf')