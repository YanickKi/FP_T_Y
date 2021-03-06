import numpy as np 
import matplotlib.pyplot as plt
import math

alpha = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180]
A = [46.412, 45.690, 36.768, 39.503, 46.703, 37.363, 42.624, 41.225, 46.546, 35.121, 46.553, 33.148, 43.051, 46.835, 34.708, 35.569, 36.909, 49.530, 44.854, 48.642, 47.420, 
    40.861, 29.593, 50.011, 50.454, 48.695, 49.776, 50.778, 51.515, 52.900, 51.570, 54.052, 54.604, 54.607, 53.672, 55.713, 54.096]

theta = np.arccos(0.5*np.cos(np.deg2rad(alpha))-0.5)

plt.polar(theta, A)
plt.savefig('build/hvarangle27.pdf')