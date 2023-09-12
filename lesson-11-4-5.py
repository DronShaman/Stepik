n = int(input())
numbers = []
li = []
for i in range(0, n):
    m = input()
    numbers.append(m)
    if numbers[i] not in li:
        li.append(m)
for j in range(0, len(li)):
    print(li[j])