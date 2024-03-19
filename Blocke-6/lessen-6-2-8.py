# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
city1 = str(input())
city2 = str(input())
city3 = str(input())
dlina_c1 = len(city1)
dlina_c2 = len(city2)
dlina_c3 = len(city3)
minomem = min(dlina_c1, dlina_c2, dlina_c3)
maximum = max(dlina_c1, dlina_c2, dlina_c3)
if dlina_c1 == minomem and dlina_c2 == maximum:
    print(city1, city2, sep="\n")

elif dlina_c2 == minomem and dlina_c1 == maximum:
    print(city2, city1, sep="\n")
elif dlina_c1 == minomem and dlina_c3 == maximum:
    print(city1, city3, sep="\n")
elif dlina_c3 == minomem and dlina_c1 == maximum:
    print(city3, city1, sep="\n")
elif dlina_c2 == minomem and dlina_c3 == maximum:
    print(city2, city3, sep="\n")
elif dlina_c3 == minomem and dlina_c2 == maximum:
    print(city3, city2, sep="\n")