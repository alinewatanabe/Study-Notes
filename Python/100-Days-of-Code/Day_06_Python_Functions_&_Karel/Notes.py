def turn_around_left():
    turn_left()
    turn_left()
def turn_right():
    i = 0
    while(i < 3):
        turn_left()
        i += 1

turn_left()
i = 0
while(i < 4):
    while(wall_in_front() == False):
        move()
    turn_right()
    i += 1