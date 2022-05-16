#ALLES IN CM
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

L = 30.8 #Abstand Gitter zu Schirm

d80l, d80r = np.genfromtxt('data_scripts/data/gitter80.txt', unpack = True)
d100l, d100r = np.genfromtxt('data_scripts/data/gitter100.txt', unpack = True)
d600l, d600r = np.genfromtxt('data_scripts/data/gitter600.txt', unpack = True)
d1200l, d1200r = np.genfromtxt('data_scripts/data/gitter1200.txt', unpack = True)

def lambda_calc(d, L, g, n):
    return np.sin(np.tan(d/L))/(g*n*10**(3))*10**9

lambda80l   = lambda_calc(d80l,     L, 80,    np.array(np.where(d80l))+1)
lambda80r   = lambda_calc(d80r,     L, 80,    np.array(np.where(d80r))+1)
lambda100l  = lambda_calc(d100l,    L, 100,   np.array(np.where(d100l))+1)
lambda100r  = lambda_calc(d100r,    L, 100,   np.array(np.where(d100r))+1)
lambda600l  = lambda_calc(d600l,    L, 600,   np.array(np.where(d600l))+1)
lambda600r  = lambda_calc(d600r,    L, 600,   np.array(np.where(d600r))+1)
lambda1200l = lambda_calc(d1200l,   L, 1200,  np.array(np.where(d1200l))+1)
lambda1200r = lambda_calc(d1200r,   L, 1200,  np.array(np.where(d1200r))+1)


lambda_mean80l = np.mean(lambda80l)
lambda_mean80r = np.mean(lambda80r)
lambda_mean100l = np.mean(lambda100l)
lambda_mean100r = np.mean(lambda100r)
lambda_mean600l = np.mean(lambda600l)
lambda_mean600r = np.mean(lambda600r)


lambda_mean = np.mean([lambda_mean80l, lambda_mean80r, lambda_mean100l, lambda_mean100r, lambda_mean600l, lambda_mean600r, lambda1200l, lambda1200r])

lambda_std = np.std([lambda_mean80l, lambda_mean80r, lambda_mean100l, lambda_mean100r, lambda_mean600l, lambda_mean600r, lambda1200l, lambda1200r]) / np.sqrt(2*(len(lambda80l)+len(lambda100l)+len(lambda600l)+len(lambda1200l)))

print(f'Die Wellenlaenge ergibt sich zu {lambda_mean} pm {lambda_std}.')
 
np.savetxt(
    'data_scripts/data/wavelength_80.txt',
   np.column_stack([d80l, lambda80l.T, d80r, lambda80r.T]),
    fmt="%10.2f, %10.2f, %10.2f, %10.2f",
    delimiter=',',
    header='Abstand links, Wellenlaenge links, Abstand rechts, Wellenlaenge rechts',
) 

np.savetxt(
    'data_scripts/data/wavelength_100.txt',
   np.column_stack([d100l, lambda100l.T, d100r, lambda100r.T]),
    fmt="%10.2f, %10.2f, %10.2f, %10.2f",
    delimiter=',',
    header='Abstand links, Wellenlaenge links, Abstand rechts, Wellenlaenge rechts',
) 

np.savetxt(
    'data_scripts/data/wavelength_600.txt',
   np.column_stack([d600l, lambda600l.T, d600r, lambda600r.T]),
    fmt="%10.2f, %10.2f, %10.2f, %10.2f",
    delimiter=',',
    header='Abstand links, Wellenlaenge links, Abstand rechts, Wellenlaenge rechts',
) 

np.savetxt(
    'data_scripts/data/wavelength_1200.txt',
   np.column_stack([d1200l, lambda1200l.T, d1200r, lambda1200r.T]),
    fmt="%10.2f, %10.2f, %10.2f, %10.2f",
    delimiter=',',
    header='Abstand links, Wellenlaenge links, Abstand rechts, Wellenlaenge rechts',
) 