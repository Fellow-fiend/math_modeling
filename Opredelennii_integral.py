import os
j = (-1)**0.5
def trapezoid_rule(func, a, b, nseg):
    """Правило трапеций
       nseg - число отрезков, на которые разбивается [a;b]"""
    dx = 1.0 * (b - a) / nseg
    sum = 0.5 * (func(a) + func(b))
    for i in range(1, nseg):
        sum += func(a + i * dx)

    return sum * dx

def function(x):
    return 5*x**2 + 1/x - x**j
print(trapezoid_rule(function, float(input("Введите нижнюю границу\n")),
                     float(input("Введите верхнюю границу\n")), 100))
os.system('pause')
