# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента
# строку text и возвращает значение True если указанный текст является палиндромом
# и False в противном случае.

# объявление функции
def is_palindrome(text):
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.replace("?", "")
    text = text.replace("...", "")
    text2 = text[::-1]
    if text == text2:
        return True
    else:
        return True


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))