n = int(input())
s = 0
for i in range(1, n+1):
    for k in range(1, i+1):
        if i % k == 0:
            s += 1
    print(str(i) + s * "+")
    s = 0