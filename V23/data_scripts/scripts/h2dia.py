import numpy as np 
import matplotlib.pyplot as plt

dia = [10, 16]
A   = [17.096, 22.208]

plt.xlabel(r'$d \mathbin{/} \si{\milli\meter}$')
plt.ylabel(r'$A$')

plt.plot(dia, A, '.')

plt.savefig('build/h2dia.pdf')