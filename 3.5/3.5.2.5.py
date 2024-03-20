from turtle import *
n = int(input('Введите кол-во лучей: '))
dot(20)
shape('triangle')
c = 360 / n
left(90)
for _ in range(n):
  forward(100)
  stamp()
  backward(100)
  right(c)
exitonclick()