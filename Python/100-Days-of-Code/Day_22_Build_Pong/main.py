from turtle import Screen
from Paddle import Paddle
from ball import Ball
from time import sleep
from score import Score

XL_POS = -350
YL_POS = 0
XR_POS = 350
YR_POS = 0
game_is_on = True

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(False)

paddle_r = Paddle(XR_POS, YR_POS)
paddle_l = Paddle(XL_POS, YL_POS)
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(fun=paddle_r.up, key="Up")
screen.onkeypress(fun=paddle_r.down, key="Down")
screen.onkeypress(fun=paddle_l.up, key="w")
screen.onkeypress(fun=paddle_l.down, key="s")

while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_v()

    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_h()

    if ball.xcor() > 410:
        ball.reset_position()
        score.point_l()

    if ball.xcor() < -410:
        ball.reset_position()
        score.point_r()


screen.exitonclick()
