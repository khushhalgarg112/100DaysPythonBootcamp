from turtle import Turtle

align = "center"
font = ("Courier", 15, "normal")


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score = {self.score}", align="center", font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
