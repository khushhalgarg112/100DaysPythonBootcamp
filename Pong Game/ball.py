from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(1)
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        x_corr = self.xcor() + self.xmove
        y_corr = self.ycor() + self.ymove
        self.goto(x_corr, y_corr)
    
    def bounce(self):
        self.ymove *= -1

    def collide(self):
        self.xmove *= -1
        self.move_speed *=0.9  

    def reposition(self):
        self.home()
        self.move_speed = 0.1
        self.collide()

        
 