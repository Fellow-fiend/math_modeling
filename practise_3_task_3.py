from numpy import *
import practise_3_task_1 as constants
kfs = 5
v0 = float(input("Speed: "))
x0 = float(input("x0: "))
y0 = float(input("y0: "))
alpha = float(input("angle in deegres: ")) * pi / 180
t = linspace(0, 5, kfs)

v0x = v0 * cos(alpha)
v0y = v0 * sin(alpha)

txy = zeros((kfs, 3))
for i in range(kfs):
  x = x0 + v0x * t[i]
  y = y0 + v0y - (constants.g * t[i]**2) / 2
  print(x, y)
  txy[i][0] = t[i]
  txy[i][1] = x
  txy[i][2] = y

print(txy)