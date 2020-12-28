import matplotlib.pyplot as plt
import numpy as np

def cycloid(r = 1):
	t = np.arange(0, 2*np.pi, 0.01)
	x = r*(t-np.sin(t))
	y = r*(1-np.cos(t))
	plt.plot(x, y, lw=1)
	plt.axis('equal')
	plt.show()

def astroid(r = 1):
	t = np.arange(0, 2*np.pi, 0.01)
	x = r*np.cos(t)**3
	y = r*np.sin(t)**3
	plt.plot(x, y, lw=1)
	plt.axis('equal')
	plt.show()