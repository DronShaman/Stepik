#192
n = int(input())
sum = 0
d = 0
while True:
    if n // 10 == 0:
        print(n)
        break
    while n != 0:
        d = n % 10
        sum += d
        n = n // 10
    if sum < 10:
        print(sum)

print(sum)