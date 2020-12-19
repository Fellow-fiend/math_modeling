import matplotlib.pyplot as plt
import numpy as np

'''def default():
	plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.title(title)
  plt.show()'''

def square_plot(xA = 0, yA = 0, A = 1, title="Square"):
	x = [xA, xA+A, xA+A, xA, xA]
	y = [yA, yA, yA+A, yA+A, yA]
	plt.plot(x, y)
	plt.axis('equal')
	plt.show() 