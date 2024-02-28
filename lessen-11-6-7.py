# На вход программе подается строка, содержащая английский текст. Напишите
# программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'

n = input()

n = n.split()
count = 0
for i in range(len(n)):
    count = (n.count("a") + n.count("A") + n.count("an") + n.count("An") +
             n.count("The")) + n.count("the")


print("Общее количество артиклей:", count)