import math
def circle(radius):
    return math.pi * radius ** 2
def rectangle(width, height):
    return width * height
def triangle(base, height):
    return 0.5 * base * height
print("Выберите фигуру:")
print("1. Круг")
print("2. Прямоугольник")
print("3. Треугольник")
choice = int(input("Введите номер фигуры: "))
if choice == 1:
    radius = float(input("Введите радиус круга: "))
    a = circle(radius)
    print(f"Площадь круга: {a}")
elif choice == 2:
    w = float(input("Введите ширину прямоугольника: "))
    h = float(input("Введите высоту прямоугольника: "))
    a = rectangle(w, h)
    print(f"Площадь прямоугольника: {a}")
elif choice == 3:
    b = float(input("Введите основание треугольника: "))
    h = float(input("Введите высоту треугольника: "))
    a = triangle(b, h)
    print(f"Площадь треугольника: {a}")
else:
    print("Выбрана неверная опция")