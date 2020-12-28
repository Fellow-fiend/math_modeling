import matplotlib.pyplot as plt
import numpy as np

def stairs(n = 10):
	x = np.arange(0, n, 0.01)
	y = x//1
	plt.plot(x, y, color="g", label="parabola")
	plt.axis('equal')
	plt.show()
