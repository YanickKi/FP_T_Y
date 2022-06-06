import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

wavelength, theta1w1, theta1m1, theta2w1, theta2m1 = np.genfromtxt('data_scripts/data/probe1.txt', unpack = True)
wavelength, theta1w2, theta1m2, theta2w2, theta2m2 = np.genfromtxt('data_scripts/data/probe2.txt', unpack = True)
wavelength, theta1w3, theta1m3, theta2w3, theta2m3 = np.genfromtxt('data_scripts/data/probe3.txt', unpack = True)


deltatheta1 = abs(theta2w1 + theta2m1/60 - theta1w1 - theta1m1/60)/2
deltatheta2 = abs(theta2w2 + theta2m2/60 - theta1w2 - theta1m2/60)/2
deltatheta3 = abs(theta2w3 + theta2m3/60 - theta1w3 - theta1m3/60)/2

plt.xlabel(r'$\lambda^2 \mathbin{/} \si{\micro\meter\squared}$')
plt.ylabel(r'$\frac{\symup{\Delta}\theta}{d} \mathbin{/} \si{\degree\per\meter}$')


plt.plot(wavelength**2, deltatheta1/(5.11e-3),'x', label = 'Undotiert')
plt.plot(wavelength**2, deltatheta3/(1.36e-3),'x', label = r'$\text{Dotiert},\; N=\num{1.2e18}, \; d = \qty{1,36}{\milli\meter}$')
plt.plot(wavelength**2, deltatheta2/(1.296e-3),'x', label = r'$\text{Dotiert},\; N=\num{2.8e18}, \; d = \qty{5,11}{\milli\meter}$')


plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/probe.pdf')

 
np.savetxt(
    'data_scripts/data/deltatheta.txt',
     np.column_stack([wavelength, deltatheta1, deltatheta3, deltatheta2]),
    fmt="%10.3f , %10.2f, %10.2f, %10.2f",
    delimiter='&',
    header='wavelength, dt1, dt2, dt3',
)  