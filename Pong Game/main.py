from turtle import Turtle, Screen
import time
from ball import Ball
from move import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
score = Scoreboard()

ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)


game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce()

    if (
        r_paddle.distance(ball) < 50
        and ball.xcor() > 320
        or l_paddle.distance(ball) < 50
        and ball.xcor() < -320
    ):
        ball.collide()

    if ball.xcor() > 380:
        ball.reposition()
        score.lpoint()

    if ball.xcor() < -380:
        ball.reposition()
        score.rpoint()

screen.exitonclick()
