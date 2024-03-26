# Напишите функцию convert_to_python_case(text),
# которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».
# объявление функции
def convert_to_python_case(text):
    s = text[0].lower()
    for i in range(1, len(text)):
        if text[i] in "abcdefghijklmnopqrstuvwxyz":
            s += text[i]
        elif text[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s += "_" + text[i].lower()
        elif text[i] in "1234567890":
            s += text[i]
    return s
# считываем данные
txt = input()
# вызываем функцию
print(convert_to_python_case(txt))