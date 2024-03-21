# Merge lists 2
# На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки
# в один отсортированный список с помощью функции quick_merge(), а затем выводит его.
def quick_merge(n):
    s = []
    for i in range(n):
        m = list(map(int, input().split()))
        s = s + m
    s = s.sort()
    for j in range(len(s)):
        print(s[j], end="")


num = int(input())

quick_merge(num)