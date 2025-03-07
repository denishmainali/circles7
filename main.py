import turtle

screen = turtle.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.bgcolor("tan")

t = turtle.Turtle()
t.speed(0)
t.pencolor("blue")
t.pensize(2)
t.penup()
t.goto(-80,15)
t.pendown()
t.circle(35)

t.penup()
t.goto(0,15)
t.pencolor("black")
t.pendown()
t.circle(35)

t.penup()
t.goto(80,15)
t.pencolor("red")
t.pendown()
t.circle(35)

t.penup()
t.goto(-40,-15)
t.pencolor("yellow")
t.pendown()
t.circle(35)

t.penup()
t.goto(40,-15)
t.pencolor("green")
t.pendown()
t.circle(35)

t.penup()
t.goto(0,100)
t.pencolor("purple")
t.pendown()
t.write("Winter Olympics", font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(0,-85)
t.pendown()
t.write("2026", font=("Arial",30,"bold"),align="center")

#No code beyond this line
turtle.done()