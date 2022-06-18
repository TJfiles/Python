"""
Implemente a função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis
olímpicos mostrados a seguir. Use a função jump() do módulo ch3. Você conseguirá obter a
imagem desenhada executando:
>>> import turtle
>>> s = turtle.Screen()
>>> t = turtle.Turtle()
>>> olimpíadas(t)
"""
'''
import turtle

s = turtle.Screen()
t = turtle.Turtle()


def olimpiadas(turtle):
    'Faz a tartaruga desenhar os anéis olímpicos'
    x = -100
    y = 0
    for i in range(5):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(50)
        x =+ 10
        y =+ 30


olimpiadas(t)
'''