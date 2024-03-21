# На вход программе подается строка текста, содержащая различные натуральные числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
# 3 4 1 2 5
# 1 9 8 7 6 5 4 3 2 10

n = input()
n = n.split()
for i in range(len(n)):
    n[i] = int(n[i])
minim = min(n)
maxim = max(n)

positio_max = n.index(maxim)
positio_min = n.index(minim)

n[positio_max ] = minim
n[positio_min] = maxim

for i in range(len(n)):
    print(n[i], sep=" ", end=" ")
