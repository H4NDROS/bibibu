import turtle

t = turtle.Turtle()
t.speed(1)
# Рисуем квадрат
for i in range(3):
    t.forward(50)
    t.right(90)
# Рисуем треугольник
t.forward(50)
t.right(30)
t.forward(50)
t.right(120)
t.forward(50)

turtle.done()