import turtle
turtle.speed(0)
turtle.bgcolor('black')
colors=['red','pink','blue','cyan','green','white','yellow']
for i in range(36):
    turtle.pencolor(colors[i%len(colors)])
    turtle.circle(90)
    turtle.left(10)
turtle.exitonclick()