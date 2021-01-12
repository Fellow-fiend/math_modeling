import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-2, 2)

xdata, ydata = [], []

def update(frame):
	xdata.append(frame)
	ydata.append(np.sin(frame))
	anim_object.set_data(xdata, ydata)
	return anim_object,

ani = FuncAnimation(fig,
 										update,
 										frames=np.arange(-np.pi, np.pi, 0.01),
 										interval=5)
ani.save('lec_7_create.animation.gif')