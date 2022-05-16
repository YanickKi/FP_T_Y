import numpy as np 
import matplotlib.pyplot as plt

d_plan, I_plan = np.genfromtxt('data_scripts/data/plankonkav.txt', unpack = True)
d_konkav, I_konkav = np.genfromtxt('data_scripts/data/konkavkonkav.txt', unpack = True)

plt.xlabel(r'$L \mathbin{/} \si{\centi\meter}$')
plt.ylabel(r'$I \mathbin{/} \si{\milli\watt}$')
plt.plot(d_plan, I_plan,'.', label = 'plan-konkav')
plt.plot(d_konkav, I_konkav,'.', label = 'konkav-konkav')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/stabilitaet.pdf') 