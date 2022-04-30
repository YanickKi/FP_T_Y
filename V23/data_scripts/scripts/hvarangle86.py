import numpy as np 
import matplotlib.pyplot as plt
import math

alpha = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180]
A = [42.299, 35.019, 30.662, 34.933, 36.837, 35.377, 37.477, 37.820, 36.848, 32.309, 22.949, 1.619, 15.810, 28.120, 43.866, 49.681, 52.335, 49.995, 50.002, 44.899, 37.391
, 9.451, 10.375, 38.970, 49.590, 55.173, 56.806, 54.727, 47.715, 27.633, 8.880, 45.891, 59.184, 61.934, 58.225, 61.987, 62.118 ]

theta = np.arccos(0.5*np.cos(np.deg2rad(alpha))-0.5)

plt.polar(theta, A)
plt.savefig('build/hvarangle86.pdf')