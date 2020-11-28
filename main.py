import task_1
import task_2
import task_3
import task_4
import task_5
import numpy as np
n = int(input())
a = np.zeros(n)
for i in range(len(a)):
	a[i] = float(input())

print("Task 1")
print(task_1.mean(a))

print("Task 2")
print()
print()
print(task_2.multiply(a))

print("Task 3")
print()
print()
print(task_3.energy(float(input("m: ")), float(input("h: ")), float(input("v: "))), " Joule")
print("Task 4")
print()
print()
print(task_4.parabola(float(input()), float(input()), int(input())))
print("Task 5")
print()
print()
shape = input("type of shape: ")
if(shape == "triangle" or shape == "Triangle"):
	print(task_5.area_triangle(float(input("h: ")), float(input("a: "))))
elif(shape == "circle" or shape == "Circle"):
	print(task_5.area_circle(float(input("r: "))))
elif(shape == "rectangle" or shape == "Rectangle"):
	print(task_5.area_rectangle(float(input("a: ")), float(input("b: "))))