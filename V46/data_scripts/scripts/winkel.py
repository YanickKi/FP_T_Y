import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


wavelength, theta1w1, theta1m1, theta2w1, theta2m1 = np.genfromtxt('data_scripts/data/probe1.txt', unpack = True)
wavelength, theta1w3, theta1m3, theta2w3, theta2m3 = np.genfromtxt('data_scripts/data/probe3.txt', unpack = True)
wavelength, theta1w2, theta1m2, theta2w2, theta2m2 = np.genfromtxt('data_scripts/data/probe2.txt', unpack = True)

theta11 = theta1w1 + theta1m1/60 
theta12 = theta2w1 + theta2m1/60 
theta21 = theta1w2 + theta1m2/60
theta22 = theta2w2 + theta2m2/60 
theta31 = theta1w3 + theta1m3/60
theta32 = theta2w3 + theta2m3/60


np.savetxt(
    'data_scripts/data/theta.txt',
     np.column_stack([theta11, theta12, theta21, theta22, theta31, theta32]),
    fmt="%10.3f, %10.3f, %10.3f, %10.3f, %10.3f, %10.3f",
    delimiter='&',
    header='11, 12, 21, 22, 31, 32',
)  