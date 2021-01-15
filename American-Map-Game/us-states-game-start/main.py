import turtle
import pandas as pd
screen = turtle.Screen()
image = "us-states-game-start\states.gif"
screen.addshape(image)
screen.title("U.S. States Game")
turtle.shape(image)

states = pd.read_csv(r"us-states-game-start\50_states.csv")
state_names = states.state.to_list()
guessed_states = []
while len(guessed_states)<50:
    user_state= screen.textinput(title=(str(len(guessed_states)),"/50"), prompt="Specify full name").title()
    if user_state in state_names:
        guessed_states.append(user_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state = states[states["state"] == user_state]
        tim.goto(int(state.x),int(state.y))
        tim.write(user_state)
    elif user_state == "exit":
        break


screen.exitonclick()