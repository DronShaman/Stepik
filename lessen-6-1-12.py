# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

minimal = min(a, b, c, d, e)
maximal = max(a, b, c, d, e)
print("Наименьшее число =", minimal)
print("Наибольшее число =", maximal)