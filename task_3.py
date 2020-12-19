import matplotlib.pyplot as plt
import numpy as np

def cicrle_plot(radius=np.array([10])):
	x = np.arange(-2 * radius[len(radius)-1], 2 *  radius[len(radius)-1], 0.1)
	y = np.arange(-2 * radius[len(radius)-1], 2 *  radius[len(radius)-1], 0.1)
	X, Y = np.meshgrid(x, y)
	plt.axis('equal')
	cicrle = X**2 + Y**2
	plt.contour(X,Y,cicrle, levels=radius**2)
	plt.show()

def ellipse_plot(a=10, b=10, radius=np.array([10])):
	x = np.arange(-10 * radius[len(radius)-1], 10 *  radius[len(radius)-1], 0.1)
	y = np.arange(-10 * radius[len(radius)-1], 10 *  radius[len(radius)-1], 0.1)
	X, Y = np.meshgrid(x, y)
	plt.axis('equal')
	ellipse = (X**2)/(a**2) + (Y**2)/(b**2) 
	plt.contour(X,Y,ellipse, levels=radius)
	plt.show()