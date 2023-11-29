a = int(input())
b = int(input())
total = 0
max_total = 0
x = 0
for i in range(a, b + 1):
    for k in range(1, i + 1):
        if i % k == 0:
            total += k
    if total >= max_total:
        max_total = total
        x = i
    total = 0
print(x, max_total, sep=" ")
