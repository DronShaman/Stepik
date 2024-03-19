# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
import math

R = float(input())
S = math.pi * R*R
C = 2 * math.pi * R
print(S)
print(C)