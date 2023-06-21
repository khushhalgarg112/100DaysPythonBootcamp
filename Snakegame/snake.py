from turtle import Turtle, Screen

corrdinates = [(0, 0), (-20, 0), (-40, 0)]
distance = 10
up = 90
down = 270
left = 180
right = 0 
class Snake:
    def __init__(self):
        self.screen = Screen()
        
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def move_clock(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_anticlock(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def move_up(self):
        if self.head.heading() != 270:    
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def create(self):
        for i in corrdinates:
            self.add_segment(i)

    def add_segment(self,position):
            tut = Turtle(shape="square")
            tut.color("white")
            tut.penup()
            tut.goto(position)
            self.segments.append(tut)

    def extends(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(10000,10000)
        self.segments = []
        self.create()
        self.head = self.segments[0]
        

    def move(self):
        
        for j in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[j - 1].xcor()
            y_cor = self.segments[j - 1].ycor()
            self.segments[j].goto(x_cor, y_cor)

        self.segments[0].forward(distance)
        self.screen.listen()
        self.screen.onkey(key="Right", fun=self.move_anticlock)
        self.screen.onkey(key="Left", fun=self.move_clock)
        self.screen.onkey(key="Up", fun=self.move_up)
        self.screen.onkey(key="Down", fun=self.move_down)





# Python inheritance

'''
class Human:
    def __init__(self) :
        self.eyes =2

    def brethe(self):
        print("Exhale,Inhale")
    

class man(Human):
    def __init__(self):
        super().__init__()

    def strength():
        print("Has more strength")

    def brethe(self):
        super().brethe()

        print("Hold Brethe for more than 4 min")

men = man()

men.brethe()
print(men.eyes)'''