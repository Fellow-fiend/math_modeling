import numpy as np
def parabola(a, b, N):
	accuracy = np.linspace(a, b, N+1)
	y = np.zeros(N)
	for i in range(N):
		y[i] = accuracy[i]**2
	return y