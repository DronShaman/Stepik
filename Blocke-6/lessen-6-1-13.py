# Напишите программу, которая упорядочивает три числа от большего к меньшему.
a = int(input())
b = int(input())
c = int(input())

mina = min(a, b, c)
maxi = max(a, b, c)
if a == b and a > c:
    print(a, b, c)
elif a == c and a > b:
    print(a, c, b)
elif b == c and b > a:
    print(b, c, a)
elif c == a and c > b:
    print(a, c, b)

if a == b and a < c:
    print(c, a, b)
elif a == c and a < b:
    print(b, a, b)
elif b == c and b < a:
    print(a, b, a)
elif c == a and c < b:
    print(b, c, c)

elif a > mina and a < maxi:
    print(maxi, a, mina, sep="\n")
elif b > mina and b < maxi:
    print(maxi, b, mina, sep="\n")
elif c > mina and c < maxi:
    print(maxi, c, mina, sep="\n")