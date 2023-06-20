from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.xmove = 10
        self.ymove = 10

    def move(self):
        x_corr = self.xcor() + self.xmove
        y_corr = self.ycor() + self.ymove
        self.goto(x_corr, y_corr)
    
    def bounce(self):
        self.ymove *= -1

    def collide(self):
        self.xmove *= -1

    def reposition(self):
        self.home()
        self.collide()

        
 