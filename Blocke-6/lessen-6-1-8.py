# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
# 3384390.4339
n = float(input())
s = int(n * 10) % 10
print(s)
