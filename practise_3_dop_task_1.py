import numpy as np
a = int(input())
b = int(input())

arr1 = np.zeros((a, b))
arr2 = np.zeros((a,b))
arr3 = np.zeros((a, b))
for i in range(a):
	for j in range(b):
		arr1[i][j] = float(input())
		arr2[i][j] = float(input())
		if arr1[i][j] >= arr2[i][j]: arr3[i][j] = arr1[i][j]
		else: arr3[i][j] = arr2[i][j]
print(arr1)
print()
print("arr2:")
print(arr2)
print()
print("arr3:")
print(arr3)