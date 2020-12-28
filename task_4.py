import matplotlib.pyplot as plt
import numpy as np

def log_spiral(b = 0.05):
	f = np.arange(0, 8*np.pi, 0.01)
	r = np.e ** (b*f)
	x = r*np.cos(f)
	y = r*np.sin(f)
	plt.plot(x, y, lw = 1)
	plt.axis('equal')
	plt.show()

def arch_spiral(k = 1):
	f = np.arange(0, 8*np.pi, 0.01)
	r = k*f
	x = r*np.cos(f)
	y = r*np.sin(f)
	plt.plot(x, y, lw = 1)
	plt.axis('equal')
	plt.show()

def rod_spiral(k = 1):
	f = np.arange(0.0001, 8*np.pi, 0.01)
	r = k/(f**0.5)
	x = r*np.cos(f)
	y = r*np.sin(f)
	plt.plot(x, y, lw = 1)
	plt.axis('equal')
	plt.show()

def rose_spiral(k = 1):
	if k <= 0: k = 1
	f = np.arange(0, 8*np.pi, 0.01)
	r = np.sin(k*f)
	x = r*np.cos(f)
	y = r*np.sin(f)
	plt.plot(x, y, lw = 1)
	plt.axis('equal')
	plt.show()
