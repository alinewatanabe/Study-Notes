import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pd.read_csv("50_states.csv")
states_list = states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        states_to_csv = []
        for state in states_list:
            if state not in guessed_states:
                states_to_csv.append(state)
        data = pd.DataFrame(states_to_csv)
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        st = turtle.Turtle()
        st.hideturtle()
        st.penup()
        state_coord = states[states.state == answer_state]
        st.goto(int(state_coord.x), int(state_coord.y))
        # st.write(state_coord.state.item())
        st.write(answer_state)


