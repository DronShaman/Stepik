# объявление функции
def print_digit_sum(num):
    n = 0
    while num > 1:
        n += num % 10
        num = num // 10
    print(n)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)