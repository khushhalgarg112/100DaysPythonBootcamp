from turtle import Turtle, Screen
import time
from scoreboard import scoreboard
from snake import Snake
from Food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake run")
screen.tracer(0)

snake = Snake()

game_on = True
# snake.create() i run this function in _init_ function
food = Food()
score = scoreboard()
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refersh()
        score.increase_score()
        snake.extends()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -280
    ):
        game_on = False
        score.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            game_on = False
            score.game_over()

screen.exitonclick()