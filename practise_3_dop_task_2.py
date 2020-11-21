import numpy as np
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())

arr = np.zeros((a1, a2, a3, a4, a5))
for i1 in range(a1):
	for i2 in range(a2):
		for i3 in range(a3):
			for i4 in range(a4):
				for i5 in range(a5):
					if i1 == a1 and i2 == a2 and i3 == a3 and i4 == a4 and i5 == a5: break
					arr[i1][i2][i3][i4][i5] == float(input())

print('Enter a value and position: ')
number = float(input())
c1 = int(input())
c2 = int(input())
temp = arr.copy()
