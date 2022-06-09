import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

d, B = np.genfromtxt('data_scripts/data/magn.txt', unpack = True)


plt.xlabel(r'$d \mathbin{/} \si{\milli\meter}$')
plt.ylabel(r'$B \mathbin{/} \si{\milli\tesla}$')
plt.plot(d, B,'x')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/magn.pdf')
