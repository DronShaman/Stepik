# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.

a = str(input())
b = str(input())
c = str(input())
a1 = len(a)
b1 = len(b)
c1 = len(c)
sred = 0
mina = min(a1, b1, c1)
maxi = max(a1, b1, c1)
if a1 != maxi and a1 != mina:
    sred = a1
elif b1 != maxi and b1 != mina:
    sred = b1
elif c1 != maxi and c1 != mina:
    sred = c1

if maxi - sred == sred - mina:
    print("YES")
else:
    print("NO")