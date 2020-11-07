import numpy as np
a = [1,2,4]
b = np.array([[0, 1, 7], [9, 12, 8]])
c = np.zeros((2,3))
d = np.ones((2, 3))
e = d*3-b
print(e)
print('\n')
print((d*3-b).transpose())
print('\n')
print(e[0, 1: :])
print(e[::, 0])
