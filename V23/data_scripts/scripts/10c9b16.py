import numpy as np 
import matplotlib.pyplot as plt

w, A = np.genfromtxt('data_scripts/data/Festkoerper/A2/10_16.dat', unpack = True)

plt.xlabel(r'$\omega \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$A$')

plt.plot(w/1000, A)

plt.savefig('build/10c9b16.pdf')