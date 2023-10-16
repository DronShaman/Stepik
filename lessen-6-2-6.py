# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
# «Hello [введенное имя] [введенная фамилия]! You have just delved into Python».

last_name = input()
first_name = input()
stroka = "Hello " + last_name + " " + first_name + "!" + " You have just delved into Python"
print(stroka)