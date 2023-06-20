from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.8, 4)
        self.goto(position)
        self.left(90)
        self.color("white")
        

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


