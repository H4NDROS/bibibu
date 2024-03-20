class Triangle_new():
    def __init__(self,a,b,c):
        if a <= 0 or b <= 0 or c <= 0:
            print('С отрицательными числами ничего не выйдет.')
        else:
            self.a = a
            self.b = b
            self.c = c
    def is_triangle(self):
        if a+b > c:
            print('Можно построить треугольник.')
        elif a+b < c or a+c<b or a+c>b:
            print('Из этих чисел треугольник не построить.')
        elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            print('Нужно вводить только числа.')
a = (input('Введите первую сторону: '))
b = (input('Введите вторую сторону: '))
c = (input('Введите третью сторону: '))
i = Triangle_new(a,b,c)
print(i.is_triangle())