# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет, интересное число или нет. Если число интересное, следует вывести «Число интересное»,
# иначе - «Число неинтересное».

n = int(input())
a = n //100
b = n //10 - a * 10
c = n % 10
mina = min(a, b, c)
maxi = max(a, b, c)

if a > mina and a < maxi and maxi - mina == a:
    print("Число интересное")
elif b > mina and b < maxi and maxi - mina == b:
    print("Число интересное")
elif c > mina and c < maxi and maxi - mina == c:
    print("Число интересное")
else:
    print("Число неинтересное")