'''from turtle import Turtle, Screen

part = Turtle()
part.color("blue")
part.shape("turtle")
# part.forward(100)
# part.right(25)
# part.setpos(20,30)
# part.position()
# part.stamp()
# part.setx(200)
# part.setheading(200)
# part.circle(30, 360,100)
# part.fd(20)
# part.dot(30,'red')
# part.fd(20)
for i in range(8):
    part.stamp(); part.fd(30)

part.clearstamp(3)

screen = Screen()
screen.exitonclick()
'''

from prettytable import PrettyTable

hi = PrettyTable()
hi.field_names = ["Pokemon", "Type", "Power", "Height in m"]
hi.add_row(["Blastoise", "Water", 90,2.5])
hi.add_row(["Charlizard", "Fire", 96,3.0])
hi.add_row(["Venasauraus", "Grass", 80,4.0])
hi.add_row(["Lucario", "Fighting", 85,2.0])
hi.add_row(["Greninja", "Water", 90,2.5])

# hi.align["Pokemon"] = 'l'
# hi.align["Type"] = 'l'
# hi.align["Height in m"] = 'l'
hi.align = 'l'
hi.border = False  # remove border

print(hi)