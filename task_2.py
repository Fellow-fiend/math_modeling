import matplotlib.pyplot as plt
import numpy as np

def parabola_plot(a=1, b=1, c=0, N=100, title="Parabola plotter"):
	x = np.arange(-N, N, 0.01)
	y = a * x**2 + b * x + c
	plt.plot(x, y, color="g", label="parabola")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.title(title)
	plt.axis('equal')
	plt.show()

def hyperbola_plot(k=10, N=1000):
	x = np.arange(-N, N, 1)
	y = k/x
	plt.plot(x, y)
	plt.show()