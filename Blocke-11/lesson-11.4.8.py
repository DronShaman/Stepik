#На вход программе подается натуральное число n, а затем
#n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули,
#а затем все положительные числа, каждое на отдельной строке.
#Числа должны быть выведены в том же порядке, в котором они были введены.

n = int(input())
num1 = []
num2 = []
num3 = []
for i in range(0, n):
    m = int(input())
    if m < 0:
        num1.append(m)
    elif m == 0:
        num2.append(m)
    elif m > 0:
        num3.append(m)
for j in range(0, len(num1)):
    print(num1[j])
for x in range(0, len(num2)):
    print(num2[x])
for y in range(0, len(num3)):
    print(num3[y])