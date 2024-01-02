import turtle
t = turtle.Turtle()
t.shape('turtle')

t.speed(7)

screen = turtle.Screen()
screen.bgcolor("sky blue")
t.hideturtle()
t.penup()

t.goto(0, -210)


t.pendown()
t.color('white')
t.fillcolor('white')
t.begin_fill()
t.circle(90)


t.goto(0, -90)
t.circle(70)

t.penup()
t.goto(0, 30)
t.circle(40)
t.end_fill()
t.color('black')
t.goto(-15,80)

t.pendown()
t.circle(4)
t.penup()

t.goto(15,80)
t.pendown()
t.circle(4)

t.penup()
t.goto(0,65)
t.pendown()

t.color('red')
t.fillcolor('orange')
t.begin_fill()
t.circle(4)
t.end_fill()
