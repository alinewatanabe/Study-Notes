from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed_cars = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance_new_car = randint(1, 6)
        if chance_new_car == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_car = randint(-230, 240)
            new_car.goto(310, y_car)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed_cars)

    def leve_up(self):
        self.speed_cars += MOVE_INCREMENT
