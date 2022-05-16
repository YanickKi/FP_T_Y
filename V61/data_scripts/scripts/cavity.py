import numpy as np 
import matplotlib.pyplot as plt

deltanu = np.array([4.85/3, 6/8, 5.9/9, 7/12, 4.7/10]) * 150e6
L_measured = np.array([63, 133, 153, 173, 210])

L_calculated = 299792458/(2*deltanu)*10**2

deviation = (L_measured-L_calculated)/L_measured * 100

np.savetxt(
    'data_scripts/data/cavity.txt',
    np.column_stack([deltanu*10**(-6), L_measured.T, L_calculated, deviation]),
    fmt="%10.1f, %3.0f, %10.2f, %10.2f",
    delimiter=',',
    header='Delta nu / kHz, L_measured / cm, L_calculated / cm, Deviation / percent',
)   