#import practise_3_tasks_4_5
#import practise_3_dop_task_1
import practise_3_dop_task_2
'''from numpy import *
# speed of light in vacuum
c = 299792458

# gravity on Earth
g = 9.81

# Gravity constant
G = 6.6743 * 10 ** (-11)

# Постоянная планка
h = 6.62607015 * 10 ** (-34)

# Постоянная Дирака
H = h/2 * pi

# elementary q
el_e = 1.602176634 * 10 ** (-19)

#постоянная Больцмана
k = 1.380649 * 10 ** (-23)

#планковская масса
m_p = (H*c / G)**0.5

#euler
e = 2.718281828
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
  y = y0 + v0y - (g * t[i]**2) / 2
  print(x, y)
  txy[i][0] = t[i]
  txy[i][1] = x
  txy[i][2] = y

print(txy)'''