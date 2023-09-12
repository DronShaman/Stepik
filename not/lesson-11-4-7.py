# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем
#k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются
# одновременно все поисковые запросы.
#5
#Язык Python прекрасен
#C# - отличный язык программирования
#Stepik - отличная платформа
#BEEGEEK FOREVER!
#язык Python появился 20 февраля 1991
#2
#язык
#python

n = int(input())

spisok = []
zapros = []

for i in range(0, n):
    a = input()
    spisok.append(a)

k = int(input())

for j in range(0, k):
    b = input()
    zapros.append(b)

for s in range(0, n):
    for g in range(0, len(rez)):
        if zapros[g].lower() in spisok[s].lower() and rez[g-1].lower() in zap[s].lower() and rez[g-2].lower() in zap[s].lower():
            z.append(zap[s])
z = list(set(z))
for i in range(0, len(z)):
    print(z[i])