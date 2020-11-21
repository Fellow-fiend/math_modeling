import numpy as np
n = int(input())
m = int(input())

A = np.zeros((n, m))
for i in range(n):
	for j in range(m):
		if i == j == 0:
			A[i][j] = np.sin(n * (i + 1) + m * (j + 1))
			if A[i][j] < 0:
				A[i][j] = 0
		else:
			A[i][j] = np.sin(n * i + m * j)
			if A[i][j] < 0:
				A[i][j] = 0
print(A)

print()
a = int(input())
b = int(input())
for i in range(n):
	A[i][a-1] += A[i][b-1]
	A[i][b-1] =  A[i][a-1] - A[i][b-1]
	A[i][a-1] -= A[i][b-1]
print(A)

# Почему бы не сделал с помощью транспонирования ?
a = int(input())
b = int(input())
A = np.transpose(A)
B = A[a-1].copy()
A[a-1] = A[b-1].copy()
A[b-1] = B.copy()
A = np.transpose(A)
print(A)