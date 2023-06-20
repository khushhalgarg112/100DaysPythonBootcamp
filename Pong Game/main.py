from turtle import Turtle, Screen
import time
from ball import Ball
from move import Paddle

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

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
    time.sleep(0.1)
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

    if ball.xcor() < -390:
        ball.reposition()

screen.exitonclick()
