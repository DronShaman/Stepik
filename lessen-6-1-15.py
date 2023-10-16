# Абсолютная сумма
# 5.4
# 33
# -1232
# -3.889
# 6
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())

sum = 0

if a1 < 0:
    a1 = a1 * (-1)
if a2 < 0:
    a2 = a2 * (-1)
if a3 < 0:
    a3 = a3 * (-1)
if a4 < 0:
    a4 = a4 * (-1)
if a5 < 0:
    a5 = a5 * (-1)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
sum = a1 + a2 + a3 + a4 + a5
print(sum)