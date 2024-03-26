# Середина отрезка

# объявление функции
def get_middle_point(x1, y1, x2, y2):
    center = (x1 + x2) / 2
    center2 = (y1 + y2) / 2
    return center, center2

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)