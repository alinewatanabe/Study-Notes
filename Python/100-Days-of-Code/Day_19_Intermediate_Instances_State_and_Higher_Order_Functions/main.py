from turtle import Turtle, Screen

roby = Turtle()
screen = Screen()

def forwards():
    roby.forward(10)

def backwards():
    roby.backward(10)

def counter_clockwise():
    roby.left(10)

def clockwise():
    roby.right(10)

def clear_drawing():
    roby.clear()
    roby.penup()
    roby.home()
    roby.pendown()


screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()