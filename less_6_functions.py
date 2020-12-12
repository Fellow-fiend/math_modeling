import matplotlib.pyplot as plt
import numpy as np


def parabola_ploter(a=1, b=1, c=0, title="Parabola plotter"):
    x = np.arange(-100, 100, 1)
    y = a * x**2 + b * x + c
    plt.plot(x, y, color="g", label="parabola")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(title)
    plt.show()


def cicrle_ploter(radius=[10]):
	x = np.arange(-2 * radius[len(radius)-1], 2 *  radius[len(radius)-1], 0.1)
	y = np.arange(-2 * radius[len(radius)-1], 2 *  radius[len(radius)-1], 0.1)
	X, Y = np.meshgrid(x, y)
	plt.axis('equal')
	cicrle = X**2 + Y**2
	plt.contour(X,Y,cicrle, levels=radius**2)
	plt.show()
