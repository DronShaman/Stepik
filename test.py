# объявление функции
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = i * fac
    return fac
def compute_binom(n, k):
    ret = factorial(n) / (factorial(k) * factorial(n - k))
    return int(ret)

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))