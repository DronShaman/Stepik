# На вход программе подается число n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в
# человеческих годах.

n = float(input())
if n >= 2:
    s = float((2 * 10.5) + (n - 2) * 4 )
else:
    s = n * 10.5
print(s)