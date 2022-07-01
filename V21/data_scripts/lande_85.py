import numpy as np
import matplotlib.pyplot as plt 

f, hori87, sweep87, hori85, sweep85 = np.genfromtxt('data_scripts/data.txt', unpack = True)


Bhori85 = np.array(8/np.sqrt(125) * 1.25663706212e-6 * 154 * hori85/15.79e-2)           #Tesla
Bsweephori85 = np.array(8/np.sqrt(125) * 1.25663706212e-6 * 11 * sweep85*0.1/16.39e-2)  #Tesla
Bhori87 = np.array(8/np.sqrt(125) * 1.25663706212e-6 * 154 * hori87/15.79e-2)           #Tesla
Bsweephori87 = np.array(8/np.sqrt(125) * 1.25663706212e-6 * 11 * sweep87*0.1/16.39e-2)  #Tesla
f = 1000*f #Hertz

B85 = Bhori85 + Bsweephori85

params85, covariance_matrix85 = np.polyfit(f, B85, deg=1, cov=True)

errors85 = np.sqrt(np.diag(covariance_matrix85))

B87 = Bhori87 + Bsweephori87

params87, covariance_matrix87 = np.polyfit(f, B87, deg=1, cov=True)

errors87 = np.sqrt(np.diag(covariance_matrix87))

f_plot = np.linspace(f[0], f[-1],100)


plt.xlabel(r'$f \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$B \mathbin{/} \si{\micro\tesla}$')
plt.plot(f, B85*10**6,'x' ,label = r'$B_{85} \, \text{gemessen}$')
plt.plot(f, B87*10**6,'x' ,label = r'$B_{87} \, \text{gemessen}$')
plt.plot(f_plot, (params85[0] * f_plot + params85[1])*10**6, label = r'$B_{85} \, \text{gefittet}$')
plt.plot(f_plot, (params87[0] * f_plot + params87[1])*10**6, label = r'$B_{87} \, \text{gefittet}$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/fits.pdf')

g85 = 6.626e-34/(9.2740100783e-24*params85[0])
g87 = 6.626e-34/(9.2740100783e-24*params87[0])
delta85 = 6.626e-34/(9.2740100783e-24*params85[0]**2) * errors85[0]
delta87 = 6.626e-34/(9.2740100783e-24*params87[0]**2) * errors87[0]

print(B85[-1])

Ez85 = g85 * 1.25663706212e-6 * B85[-1] + (g85 * 1.25663706212e-6 * B85[-1])**2 * (1-6)/(2.01e-24)
Ez87 = g87 * 1.25663706212e-6 * B87[-1] + (g87 * 1.25663706212e-6 * B87[-1])**2 * (1-4)/(4.53e-24)
deltaEz85 = 1.25663706212e-6 * B85[-1] + 2 * g85*(1.25663706212e-6 * B85[-1])**2 * (1-6)/(2.01e-24) * delta85 
deltaEz87 = 1.25663706212e-6 * B87[-1] + 2 * g87*(1.25663706212e-6 * B87[-1])**2 * (1-4)/(4.53e-24) * delta87


print(f'Der Fitparameter a85 beträgt {params85[0]} pm {errors85[0]}')
print(f'Der Fitparameter b85 beträgt {params85[1]} pm {errors85[1]}')
print(f'Der Fitparameter a87 beträgt {params87[0]} pm {errors87[0]}')
print(f'Der Fitparameter b87 beträgt {params87[1]} pm {errors87[1]}')
print(f'g85 beträgt {g85} pm {delta85}')
print(f'g87 beträgt {g87} pm {delta87}')
print(f'Der Kernspin von Rb85 ist {0.5*(2/g85 - 1)} pm {0.5 * 2*delta85/g85**2}')
print(f'Der Kernspin von Rb87 ist {0.5*(2/g87 - 1)} pm {0.5 * 2*delta87/g87**2}')
print(f'Maximale B85 ist {B85[-1]*10**6}')
print(f'Maximale B87 ist {B87[-1]*10**6}')
print(f'Die Zeemannaufspaltung Ez85 beträgt {Ez85*10**(9)} pm {deltaEz85*10**(9)}')
print(f'Die Zeemannaufspaltung Ez85 beträgt {Ez87*10**(9)} pm {deltaEz87*10**(9)}')