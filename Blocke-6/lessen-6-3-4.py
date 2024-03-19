# Средние значения
# В математике выделяют следующие средние значения:
import math

a = float(input())
b = float(input())

s1 = (a + b) / 2
s2 = math.sqrt(a * b)
s3 = (2 * a * b) / (a + b)
s4 = math.sqrt((a * a + b * b) / 2)
print(s1, s2, s3, s4, sep="\n")