# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанному промежутку.
# -1 до 17 без включения
x = int(input())
if -1 < x < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")