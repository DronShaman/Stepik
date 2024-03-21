#Дополните приведенный код, чтобы он:

# 1 Заменил второй элемент списка на 17;
# 2 Добавил числа 4, 5 и 6 в конец списка;
# 3 Удалил первый элемент списка;
# 4 Удвоил список;
# 5 Вставил число 25 по индексу 3;
# 6 Вывел список, с помощью функции print()


numbers = [8, 9, 10, 11]

numbers.remove(9)
numbers.insert(1, 17)
print(numbers)

numbers.insert(4, 4)
numbers.insert(5, 5)
numbers.insert(6, 6)
print(numbers)

del numbers[0]
print(numbers)


numbers = numbers + numbers
print(numbers)

numbers.insert(3, 25)
print(numbers)


