import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

# Definir coordenadas do queixo do rosto
x = -100
y = 50
t.penup()
t.goto(x, y)  # Move para as coordenadas
t.pendown()

# Desenhar um círculo
t.circle(100)

# Mover para olho esquerdo e desenhar
t.penup()
t.goto(x - 35, y + 120)
t.pendown()
t.dot(25)

# Saltar para olho direito
t.penup()
t.goto(x + 35, y + 120)
t.pendown()
t.dot(25)

# Desenhar o sorriso
t.penup()
t.goto(x - 60.62, y + 65)
t.pendown()
t.setheading(-60)
t.circle(70, 120)
