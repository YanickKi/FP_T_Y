import numpy as np 
import matplotlib.pyplot as plt

w, A = np.genfromtxt('data_scripts/data/Wasserstoffmolekuel/A2/0.dat', unpack = True)

plt.xlabel(r'$\omega \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$A$')

plt.plot(w/1000, A)

plt.savefig('build/h2plot.pdf')