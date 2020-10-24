import os
a = [0, 0, 0]
i = 0
for i in range(3):
	a[i] = int(input())
print(a[0]*a[1]**(a[2]-1))
os.system("PAUSE")