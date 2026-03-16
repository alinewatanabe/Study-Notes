from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)


    def up(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        self.goto(x_pos, y_pos + 20)

    def down(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        self.goto(x_pos, y_pos - 20)
