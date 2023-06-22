import turtle
import pandas as pd
import time

screen = turtle.Screen()
image = "india_map.gif"
screen.title("India State game")
screen.screensize(600, 1000)
screen.addshape(image)

tut = turtle.Turtle()
tut.shape(image)

state_name = screen.textinput(title="Guess the State", prompt="Guess State of India").title()

data = pd.read_csv("state.csv")
state_list = data.state.tolist()


def write_on_screen(x, y, state, size):
    tur = turtle.Turtle()
    tur.penup()
    tur.hideturtle()
    tur.goto(x, y)
    tur.write(state, align="center", font=("Arial", size, "bold"))

guessed_state = []
count = 0
game_on = True
while game_on:
    
    if state_name in state_list:
        count += 1
        state_list.remove(state_name)
        data_row = data[data.state == state_name]
        x_cor = data_row.x
        y_cor = data_row.y
        write_on_screen(int(x_cor), int(y_cor), state_name, 10)
    state_name = screen.textinput(
        title=f"{count}/ 28 States", prompt="Guess Another State of India"
    ).title()
    if state_name == "Exit":
        game_on = False
        pd.DataFrame(state_list).to_csv("missed_states.csv")

    

    if count == 28:
        write_on_screen(77, 179, "You Win", 25)
        time.sleep(5)
        game_on = False
        
        

