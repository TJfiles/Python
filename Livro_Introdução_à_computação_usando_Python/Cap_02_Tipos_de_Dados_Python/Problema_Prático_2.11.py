import turtle
s = turtle.Screen()
t = turtle.Turtle(shape='turtle')
t.penup()
t.goto(-300, 0)
t.pendown()
t.right(45)
t.circle(50, 90)
for i in range(1, 9):
    t.right(90)
    t.circle(50, 90)
t.penup()
t.goto(-100, 200)
t.pendown()
t.circle(50)
t.penup()
t.goto(0, -50)