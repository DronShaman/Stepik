#На вход программе подается натуральное число n, затем n строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.


n = int(input())
zap = []
rez = []

for i in range(0, n):
    m = input()
    zap.append(m)
new = input()

for i in range(0, n):
    if new.lower() in zap[i].lower():
        print(zap[i])

# Костин рабочий вариант
#d = [input() for _ in range(int(input()))]
#query = input()
#[print(s) for s in d if query.lower() in s.lower()]