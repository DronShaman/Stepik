# Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

command = str(input())
n = len(command)
#print(n)
stroka = "Футбольная команда " + str(command) + " имеет длину " + str(n) + " символов"
print(stroka)