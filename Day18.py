from turtle import Turtle, Screen, colormode
import random

part = Turtle()
part.color(
    "red", "green"
)  # here red is clocr of pen border and green is its fill color
part.speed(0)
# while True:
#     part.forward(100)
#     part.right(170)

# part.fillcolor("black")

# Challenge no 1 Draw a square
"""part.forward(100)
part.right(90)
part.forward(100)
part.right(90)
part.forward(100)
part.right(90)
part.forward(100)

"""

# Challenge no 2  importing techniquea
"""import turtle 
from turtle import Turtle
from turtle import *
import turtle as t"""

# Challenges no 3 Dashed line

"""for _ in      range(15):
    part.pendown()
    part.forward(10)
    part.penup()
    part.forward(10)
"""

# Challenge no 4 Mix Shapes
"""n = 3
part.pensize(3)
# angle = 180
for _ in range(8):
    each_angle = 360 / n
    # each_angle = angle/3
    for i in range(n):
        part.forward(50)
        part.right(each_angle)
        # part.right(180 - each_angle)

    n += 1
    # angle+=180
    # part.home()"""

# Challenge no 5 Random Walk

# choice = ['blue','brown','red','black','magenta','cyan','yellow','pink']

"""colormode(255)
def random_color():
    r  = random.randint(0,255)
    g  = random.randint(0,255)
    b  = random.randint(0,255)
    col = (r,g,b)
    return col

part.pensize(6)

dir = [0,90,180,270]
for _ in range(200):
    part.color(random_color())
    part.forward(20)
    part.setheading(dir[random.randint(0,3)])
    """

# Challenge no 6 Spirograph
"""
we can also do it using heading 
curr_head = part.heading()
part.setheading(curr_head+gap)
"""

"""colormode(255)
def random_color():
    r  = random.randint(0,255)
    g  = random.randint(0,255)
    b  = random.randint(0,255)
    col = (r,g,b)
    return col

part.pensize(3)

def draw(gap):
    for _ in range(int(360/gap)):
        part.circle(100)
        part.color(random_color())
        part.right(gap)
    
draw(10)"""


# Final Project of Dot painting

# import colorgram

"""rgb_color = []
colors = colorgram.extract('img.jpg', 40)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_color.append(new_color)

print(rgb_color)"""
colormode(255)
colors = [
    (242, 243, 245),
    (230, 228, 224),
    (236, 241, 238),
    (241, 236, 240),
    (198, 159, 116),
    (70, 92, 129),
    (147, 85, 53),
    (218, 210, 116),
    (138, 160, 191),
    (178, 160, 38),
    (184, 146, 164),
    (28, 32, 46),
    (58, 34, 23),
    (120, 70, 93),
    (139, 175, 154),
    (77, 115, 79),
    (143, 25, 16),
    (186, 97, 82),
    (61, 31, 42),
    (121, 27, 41),
    (45, 58, 94),
    (177, 96, 114),
    (102, 119, 170),
    (34, 52, 45),
    (100, 160, 85),
    (214, 175, 192),
    (216, 181, 173),
    (160, 209, 191),
    (67, 86, 23),
    (219, 206, 8),
    (181, 186, 213),
    (46, 72, 57),
    (168, 201, 212),
    (100, 137, 144),
]

part.hideturtle()

part.setheading(225)
part.penup()
part.forward(300)
part.setheading(0)
for j in range(10):
    for i in range(10):
        part.pendown()
        part.dot(20, colors[random.randint(0, 33)])
        part.penup()
        part.forward(50)

    part.setheading(90)
    part.penup()
    part.forward(50)
    part.setheading(180)
    part.forward(500)
    part.setheading(0)


screen = Screen()
screen.exitonclick()
