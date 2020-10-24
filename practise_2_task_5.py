a = int(input())
b = int(input())
if(b != 0 and a % b == 0):
  print("Делится, остаток: ", a % b, " Частное: ", a // b)
elif(b == 0): print("division by zero")
else: print("Не делится, остаток: ", a % b, " Частное: ", a // b)
