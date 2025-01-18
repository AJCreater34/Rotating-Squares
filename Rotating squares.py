import turtle
turtle.speed("fastest") 
turtle.penup()
turtle.width(5)
turtle.goto(-50,50)
turtle.pendown()
for _ in range(5):
    for _ in range(4):
        turtle.forward(150)
        turtle.right(90)
    turtle.right    (72)
turtle.hideturtle()
turtle.done()
