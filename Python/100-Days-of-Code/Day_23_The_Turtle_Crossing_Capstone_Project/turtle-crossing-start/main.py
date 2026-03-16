import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(fun=player.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() < -270:
        player.goto(0, -270)

    if player.ycor() > 290:
        score.level += 1
        score.upload_score()
        player.reset_player()
        car.leve_up()

    car.create_cars()
    car.move_cars()

    for Car in car.all_cars:
        if Car.distance(player) < 17:
            game_is_on = False
            score.game_over()

screen.exitonclick()
