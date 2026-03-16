import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors_list = ["red","orange","yellow","green","blue","purple"]
y_ini = -125
is_race_on = False
all_turtles = []

for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors_list[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_ini)
    all_turtles.append(new_turtle)
    y_ini += 50


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()