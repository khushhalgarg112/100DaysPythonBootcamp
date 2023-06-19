import random
from turtle import Turtle, Screen


# Drawing program
"""def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clock():
    tim.right(10)

def move_anticlock():
    tim.left(10)

def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_anticlock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
"""


# Turtle race game

game_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(
    title="Lets choose your turtle", prompt="Which color turtle will win the race "
)
color = ["red", "blue", "green", "yellow", "purple", "orange"]
all_turtle = []

a = 1
b = 40
for i in color:
    tut = Turtle(shape="turtle")
    tut.color(i)
    tut.penup()
    tut.goto(x=-240, y=150 - b)
    b += 40
    all_turtle.append(tut)

while game_on:
    for i in all_turtle:
        if i.xcor() > 220:
            game_on = False
            win = i.pencolor()
            if user_input == win:
                print(f"You {user_input} turtle have won the race")
            else:
                print(f"You {user_input} turtle have lost the race and the {win} turtle has won the race")
            break
        i.forward(random.randint(1, 10))


# tut.forward(50)


screen.exitonclick()
