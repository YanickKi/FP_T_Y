import numpy as np 
import matplotlib.pyplot as plt

w, A = np.genfromtxt('data_scripts/data/Festkoerper/A3/625Zylinder_10Blende.dat', unpack = True)

plt.xlabel(r'$\omega \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$A$')

plt.plot(w/1000, A)

plt.savefig('build/10c9b625.pdf')