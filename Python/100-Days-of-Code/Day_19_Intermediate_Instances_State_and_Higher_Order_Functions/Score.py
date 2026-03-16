from turtle import Turtle
ALIGNMENT = "center"
MOVE = False
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.setposition(0, 270)
        self.write(arg=f"Score: {self.score} ", move=MOVE, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} ", move=MOVE, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
