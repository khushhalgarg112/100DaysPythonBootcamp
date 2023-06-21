from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_front(self):
        self.forward(MOVE_DISTANCE)

    def level_complete(self):
        self.goto(STARTING_POSITION)
        
    def level_complete_increase_speed(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            pass


