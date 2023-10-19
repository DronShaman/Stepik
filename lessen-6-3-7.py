# Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
# Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
import math

a = float(input())
b = float(input())
c = float(input())

D = b * b - 4 * a * c
print(D)
if D > 0:
    x1 = (-1 * b - math.sqrt(D)) / (2 * a)
    x2 = (-1 * b + math.sqrt(D)) / (2 * a)
    if x1 > x2:
        print(x2)
    else:
        print(x2)
elif D < 0:
    print("Нет корней")
elif D == 0:
    x1 = (-1 * b )/ (2 * a)
    print(x1)