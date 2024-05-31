# В службе по дорожному движению решили оптимизировать процесс создания автомобильных номеров: вместо человека генерацию
# автомобильных номеров поручили некоторой GPT (модели машинного обучения).
# Как мы знаем, искусственный интеллект еще сыроват и делает много ошибок, поэтому его результаты следует тщательно проверять.
# Корректный автомобильный номер (в России) имеет следующий формат:

number = input()
if len(number) < 9:
     print("NO")
elif len(number) == 8 and number[9] in "АВЕКМНОРСТУХ":
     print("NO")
elif (number[0] in "АВЕКМНОРСТУХ" and number[1] in "1234567890" and number[2] in "1234567890" and number[
    3] in
"1234567890" and number[4] in "АВЕКМНОРСТУХ" and number[5] in "АВЕКМНОРСТУХ" and number[6] == "_" and number[7] in "1234567890"
        and number[8] in "1234567890") and len(number) == 9:
    print("YES")
elif (number[0] in "АВЕКМНОРСТУХ" and number[1] in "1234567890" and number[2] in "1234567890" and number[
3] in
"1234567890" and
        number[4] in "АВЕКМНОРСТУХ" and number[5] in "АВЕКМНОРСТУХ" and number[6] == "_" and number[7] in "1234567890" and
        number[8] in "1234567890" and number[9] in "1234567890") and len(number) == 10:
    print("YES")
else:
    print("NO")