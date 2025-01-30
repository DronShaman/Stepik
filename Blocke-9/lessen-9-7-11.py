a = input()
eng = "eyopaxcETOPAHXCBM"
rus = "еуорахсЕТОРАНХСВМ"
b = []
A = 0
for i in range(len(a)):
    A += ord(a[i])
B = 0
for j in range(len(a)):
    if a[j] in eng:
        index_my = eng.index(a[j])
        b.append(rus[index_my])
    else:
        b.append(a[j])
for x in range(len(b)):
    B += ord(b[x])
A *= 3
B *= 3
print(f"Старая стоимость: {A}🐝")
print(f"Новая стоимость: {B}🐝")