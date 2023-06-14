import math
"""
def  greet(a):
    print(f"Hello {a}")
    print(f"hola {a}")
    print(f"Namaste {a}")

greet("Hari")"""

"""def greet_with_loc(name, loc):
    print(f"Hello {name}")
    print(f"You live in {loc}")

# greet_with_loc("Anthony", "Tokyo") positional argument
greet_with_loc(loc="huwai", name="James") # keyword argument"""

# Challenge no 1

h = int(input("Enter the height of the wall "))
w = int(input("Enter the width of the wall "))
coverage = 5


def can_used(height, width, cover):
    can = (height * width) / cover
    print(f"Total paint can are used is {math.ceil(can)}")


can_used(height=h, width=w, cover=coverage)
