# Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
# Площадь правильного многоугольника с длиной стороны
# a и количеством сторон n вычисляется по формуле:
import math

n = int(input())
a = float(input())
S = (n * a * a) / (4 * math.tan(math.pi/n))
print(S)