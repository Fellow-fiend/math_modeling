import math
a = int(input())
n = int(math.log(a, 10))
temp = 0
for i in range(n):
  temp += ((a // (10**i)) % 10) * 10**(n-i)
temp += a // (10**n)
print(temp)
