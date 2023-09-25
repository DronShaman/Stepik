# На вход программе подается строка текста, содержащая различные натуральные числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
# 3 4 1 2 5
# 1 9 8 7 6 5 4 3 2 10


stroka : str = input()

list = list(stroka)
print(list)
max_number = max(list)
min_number = min(list)
positio_max = list.index(max_number)
positio_min = list.index(min_number)

list.insert(positio_min, max_number)
list.insert(positio_max, min_number)
print(list)
print(positio_max)

