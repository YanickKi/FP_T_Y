import numpy as np 
import matplotlib.pyplot as plt

w, A = np.genfromtxt('data_scripts/data/Wasserstoffatom/A4/9mm.dat', unpack = True)

plt.xlabel(r'$\omega \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$A$')

plt.plot(w/1000, A)

plt.savefig('build/h9ring.pdf')