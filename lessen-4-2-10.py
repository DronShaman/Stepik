# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.

x = int(input())
if x > -30 and x <= -2 or x > 7 and x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")