from turtle import *
penup()
goto(-400,0)
pendown()
def trg():
    pencolor('green')
    pensize(10)
    begin_fill()
    for i in range(3):
      forward(200)
      left(120)
    color("green nezhno")
    end_fill()
    color('green')
    forward(200)
for i in range (4):
  trg()
right(180)
for i in range(4):
  trg()
exitonclick()