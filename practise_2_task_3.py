a = int(input())
if not(a % 400):
  print("Високосный")
elif not(a % 100):
  print("Невисокосный")
elif not(a % 4):
  print("Високосный")
else: print("Невисокосный")
