import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
plt.axis('equal')
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-2*np.pi, 2*np.pi)

def circle(r0, t):	
	phi = np.arange(0, 2*np.pi, 0.01)
	r = r0 * t
	x = r*np.cos(phi)
	y = r*np.sin(phi)

	return x, y

def update(frame):
	anim_object.set_data(circle(0.1, frame))

anim = FuncAnimation(fig, update, frames = 500, interval=30)
anim.save('circle_move.gif')