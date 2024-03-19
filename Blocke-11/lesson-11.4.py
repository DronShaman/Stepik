#Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers
n = int(input())
numbers = []
for i in range(0, n):
    m = int(input())
    numbers.append(m)

for i in range(0, n):
    print(numbers[i])
print("\n")
for i in range(0, n):
    s = numbers[i] * numbers[i] + 2 * numbers[i] + 1
    print(s)