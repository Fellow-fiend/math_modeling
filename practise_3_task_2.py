import numpy as np
a = np.pi / 3
b = np.pi / 6
g = 9.81
h = 100
v = ( (g * h * (np.tan(b)) ** 2) / ( 2 * (np.cos(a) ** 2) * (1 - np.tan(b) * np.tan(a))))**0.5

from numpy import *
import practise_3_task_1 as contsants

T = 200
eps = 300

part1 = 2 / pi ** 0.5
part2 = contsants.H / (contsants.k * T)**1.5
part3 = e ** (-eps/(contsants.k*T))
part4 = eps ** (T/2)
N = part1 * part2 * part3 * part4



print(N)
print(v)