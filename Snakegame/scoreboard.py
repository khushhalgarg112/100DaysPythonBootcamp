from turtle import Turtle

align = "center"
font = ("Courier", 15, "normal")


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score = {self.score}  Highest Score = {self.high_score}", align="center", font=font)


    def high_score_change(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score =0 
        self.update()
        

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align="center", font=font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
