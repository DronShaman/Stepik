# Цвет настроения синий
# Напишите программу, которая считывает одну строку, после чего выводит «YES»,
# если во введенной строке есть подстрока «синий» и «NO» - в противном случае.

stroka = str(input())

if "синий" in stroka:
    print("YES")
else:
    print("NO")