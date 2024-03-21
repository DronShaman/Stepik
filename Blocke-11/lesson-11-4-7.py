# решение чата jpd который я н полностью понимаю
# Функция для проверки, содержит ли строка все поисковые запросы
def contains_all_queries(string, queries):
    for query in queries:
        if query not in string:
            return False
    return True

# Считываем количество строк и сами строки
n = int(input())
strings = [input() for _ in range(n)]

# Считываем количество поисковых запросов и сами запросы
k = int(input())
queries = [input() for _ in range(k)]

# Ищем и выводим строки, содержащие все поисковые запросы
for string in strings:
    if contains_all_queries(string, queries):
        print(string)