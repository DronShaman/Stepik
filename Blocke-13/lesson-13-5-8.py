# BEEGEEK
#
# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
# - число a – должно быть палиндромом;
# - число b – должно быть простым;
# - число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является
# действительным паролем BEEGEEK банка и False - в противном случае.

# объявление функции
def is_valid_password(password):
    m = list(map(int, password.split(":")))
    if len(m) != 3:
        return False
    a = str(m[0])
    b = m[1]
    c = m[2]
    flag1 = False
    flag2 = False
    flag3 = False
    if a == a[::-1]:
        flag1 = True
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            return False
        flag2 = True
    if c % 2 == 0:
        flag3 = True
    return flag1 and flag2 and flag3

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))