# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
if b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
if c > a and c > b:
    if b > a:
        print(b)
    else:
        print(a)