# Дано положительное действительное число. Выведите его дробную часть.
# 44.45
# 39483.2
n = float(input())
if n > 10000:
    n = n - n // 1
    print(n)
elif n > 1000:
    n = n - n // 1
    print(n)
elif n > 100:
    n = n - n // 1
    print(n)
elif n > 10:
    n = n - n // 1
    print(n)
elif n > 1:
    n = n - n // 1
    print(n)