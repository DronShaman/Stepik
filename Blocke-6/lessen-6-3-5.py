# Тригонометрическое выражение
# Напишите программу, вычисляющую значение тригонометрического выражения
import math

x = float(input())
x = math.radians(x)
s = math.sin(x) + math.cos(x) + math.tan(x)*math.tan(x)
# print(x)
# R = (x * math.pi) / 180
print(s)