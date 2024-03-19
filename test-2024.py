# объявление функции
def get_next_prime(num):
    while True:
        num += 1
        s = 0
        for i in range(1, num + 1):
            if num % i == 0:
                s += 1
        if s == 2:
            return num
        else:
            s = 0
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))