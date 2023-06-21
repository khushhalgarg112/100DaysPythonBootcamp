from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.car = []
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create(self):
        num = random.randint(1,5)
        if num ==1:
            tut = Turtle()
            tut.shape("square")
            tut.penup()
            tut.shapesize(1, 2)
            tut.color(COLORS[random.randint(0, 5)])
            tut.goto(320, random.randint(-250, 250))
            self.car.append(tut)
            self.move()
        
    def move(self):
        for _ in self.car:
            _.backward(self.car_speed)

    def inc_speed(self):
        self.car_speed += MOVE_INCREMENT
    
