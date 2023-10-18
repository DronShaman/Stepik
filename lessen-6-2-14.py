# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
# Напишите программу проверяющую корректность email адреса.

mail = str(input())

if "." in mail and "@" in mail:
    print("YES")
else:
    print("NO")