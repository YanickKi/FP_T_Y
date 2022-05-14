import numpy as np 
import matplotlib.pyplot as plt


d = np.array([3, 6, 9])
delta = np.array([2286.000-2224.000, 2271.000-2158.000, 2262.000-2089.000])


plt.xlabel(r'$d \mathbin{/} \si{\milli\meter}$')
plt.ylabel(r'$\symup{\Delta}\omega \mathbin{/} \si{\kilo\hertz}$')

plt.plot(d, delta/1000, '.')

plt.savefig('build/h3ring.pdf')