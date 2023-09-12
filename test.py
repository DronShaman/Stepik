#5
#Язык Python прекрасен
#C# - отличный язык программирования
#Stepik - отличная платформа
#BEEGEEK FOREVER!
#язык Python появился 20 февраля 1991
#2
#язык
#python
n = int(input())

strings = []
for _ in range(n):
    s = input()
    strings.append(s)

k = int(input())

search_queries = []
for _ in range(k):
    search_query = input()
    search_queries.append(search_query)

for s in strings:
    for search_query in search_queries:
        if search_query.lower() not in s.lower():
            break
    else:
        print(s)