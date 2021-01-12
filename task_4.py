import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
plt.axis('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def fractal(x0, y0, C, D, n):
	x, y = [x0], [y0]
	for i in range(n):
		x.append(x[i]**2 - y[i]**2 + C)
		y.append(2*x[i]*y[i]+D)
	plt.plot(x, y)
	plt.show()
fractal(0.1, 0.1, 0.3, 1/3, 100)