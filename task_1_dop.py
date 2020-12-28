import matplotlib.pyplot as plt
import numpy as np

def Lissajous_curve(A = 1, B = 1, a = 1, b = 1, d = np.pi / 2):
	t = np.arange(0, 8*np.pi, 0.01)
	x = A*np.sin(a*t + d)
	y = B*np.sin(b*t)
	plt.plot(x, y, lw = 1)
	plt.axis('equal')
	plt.show()
