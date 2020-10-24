a = int(input())
b = int(input())
c = int(input())
if(a + b > c and a + c > b and b + c > a):
  if(a == b == c): print("равносторонний")
  elif(a != b != c): print("разносторонний")
  else: print("равнобедренный")
else: print("Ты такие вещи не говори")
