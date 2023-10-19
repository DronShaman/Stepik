# Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n включительно.

m = int(input())
n = int(input())

if m > n:
    for i in range(n, m):
        print(i)
else:
    for i in range(n+1, m, -1):
        print(i)
