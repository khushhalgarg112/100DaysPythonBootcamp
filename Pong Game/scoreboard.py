from turtle import Turtle

Font = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=Font)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=Font)

    def lpoint(self):
        self.clear()
        self.l_score += 1
        self.update()

    def rpoint(self):
        self.clear()
        self.r_score += 1
        self.update()
