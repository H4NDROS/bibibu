import turtle
turtle.speed(0)
turtle.bgcolor('black')
colors=['red','purple','blue','green','yellow','orange']
for i in range(299):
    turtle.pencolor(colors[i%len(colors)])
    turtle.width(i/100+1)
    turtle.forward(i)
    turtle.left(59)
turtle.exitonclick()