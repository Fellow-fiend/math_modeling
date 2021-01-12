import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
plt.axis('equal')
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-2*np.pi, 2*np.pi)

def circle(r, vx0, vy0, t, x0 = 0, y0 = 0):
	x0 += vx0*t
	y0 += 0
	phi = np.arange(0, 2*np.pi, 0.01)
	x = x0 + r*np.cos(phi)
	y = y0 + r*np.sin(phi)

	return x, y

def update(frame):
	anim_object.set_data(circle(r = 1, vx0 = 0.1, vy0 = 0, t = frame))

anim = FuncAnimation(fig, update, frames = np.arange(-100, 100, 0.1), interval=30)
anim.save('circle_move.gif')