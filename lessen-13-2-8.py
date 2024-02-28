# объявление функции
def draw_triangle(fill, base):
    if base % 2 == 0:
        for i in range(1, base//2 + 1):
            print(fill * i)
        for j in range(base//2, 0, -1):
            print(fill * j)
    else:
        for i in range(base//2+1):
            print(fill * i)
        for i in range(base//2+1, 0, -1):
            print(fill * i)
    pass
# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)