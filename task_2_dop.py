import matplotlib.pyplot as plt
import numpy as np

def ellipse(p = 1/3, e = 0.5):
	if e > 1: e = 1/2
	f = np.arange(0, 8*np.pi, 0.01)
	r = p / (1 + e * np.cos(f))
	x = r*np.cos(f)
	y = r*np.sin(f)
	plt.plot(x, y, lw = 1)
	plt.axis('equal')
	plt.show()