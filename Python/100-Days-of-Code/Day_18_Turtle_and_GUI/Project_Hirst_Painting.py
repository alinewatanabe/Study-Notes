# Project Hist Painting
from turtle import Turtle, Screen, colormode
from random import choice

pen = Turtle()
pen.shape("arrow")
colors_list = [(202, 163, 98), (45, 97, 147), (168, 49, 80), (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (223, 208, 22), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78)]
c = -200
colormode(255)
pen.speed("fastest")
pen.hideturtle()
pen.up()

for a in range(10):
    pen.setx(-200)
    pen.sety(c)
    for i in range(10):
        pen.pensize(20)
        pen.pencolor(choice(colors_list))
        pen.pendown()
        pen.forward(1)
        pen.penup()
        pen.forward(50)
    pen.up()
    c += 50

screen = Screen()
screen.exitonclick()