n = int(input())
numbers = []
z = []
for i in range(0, n):
    m = int(input())
    numbers.append(m)
    z.append(m)
z.sort()
a = z[0]
b = z[-1]
numbers.remove(a)
numbers.remove(b)
print(numbers)
for j in range(0, len(numbers)):
    print(numbers[j])