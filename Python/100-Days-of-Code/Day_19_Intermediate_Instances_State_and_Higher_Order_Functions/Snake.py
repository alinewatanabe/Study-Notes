from turtle import Turtle
COORD = [(0, 0), (-20, 0), (-40, 0)]
MOVE_D = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
class Snake:
    def __init__(self):
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]

    def create_snake(self):
        for positions in COORD:
            self.add_segment(positions)


    def add_segment(self, positions):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(positions)
        self.segments_list.append(new_square)

    def extend(self):
        self.add_segment(self.segments_list[-1].position())

    def move(self):
        for seg_num in range(len(self.segments_list) - 1, 0, -1):
            new_x = self.segments_list[seg_num - 1].xcor()
            new_y = self.segments_list[seg_num - 1].ycor()
            self.segments_list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_D)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

