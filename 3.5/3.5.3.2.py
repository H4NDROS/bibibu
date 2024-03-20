from turtle import *
speed(10)
colors = ['black','white','#d9dddc','black']
a = 240
for i in range(4):
    color(colors[i%len(colors)])
    fillcolor(colors[i%len(colors)])
    begin_fill()
    for n in range(4):
        fd(a)
        lt(90)
    end_fill()
    a -= 60
exitonclick()