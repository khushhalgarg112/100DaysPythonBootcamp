import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score_update = Scoreboard()


screen.listen()
screen.onkeypress(key="Up", fun=player.move_front)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()

    for cars in car.car:
        if player.distance(cars) < 20:
            game_is_on = False
            score_update.game_over()

    if player.level_complete_increase_speed():
        player.level_complete()
        car.inc_speed()
        score_update.incerse_level()


screen.exitonclick()
