from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("blue")
        self.refersh()

    def refersh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 260)
        self.goto(x_cor, y_cor)
