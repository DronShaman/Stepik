import math

n = int(input())

a = 0
for i in range(1, n+1):
    a = a + (1 / i)

print(a - math.log(n))

