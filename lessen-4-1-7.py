# Напишите программу, которая определяет, разрешен ли пользователю доступ к интернет-ресурсу или нет.
age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")