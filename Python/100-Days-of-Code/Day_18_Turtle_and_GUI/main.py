from turtle import Turtle, Screen
from random import random, choice

# Challeng 01 - Draw a Square
"""tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine3")"""

#for i in range(4):
#    tim.forward(100)
#    tim.left(90)

# Challeng 02 - Dashed Line
"""for i in range(15):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()"""

# Challeng 03 - Drawing Different
"""side = 3
while(side < 10):
    R = random()
    G = random()
    B = random()
    for i in range(side):
        tim.pencolor(R, G, B)
        tim.forward(100)
        tim.right(360/side)
    side += 1"""

# Challeng 04 - Random Walk
"""tim.speed("fast")
directions = [0, 90, 180, 270]
tim.pensize(10)

for i in range(200):
    R = random()
    G = random()
    B = random()
    tim.pencolor(R, G, B)
    tim.forward(20)
    tim.setheading(choice(directions))"""

# Challenge 05
"""tim.speed("fastest")
ang = 1

for i in range(int(360/ang)):
    R = random()
    G = random()
    B = random()
    tim.pencolor(R,G,B)
    tim.circle(100)
    tim.left(ang)
    
    screen = Screen()
    screen.exitonclick()"""



