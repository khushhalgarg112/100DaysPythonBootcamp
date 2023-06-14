
'''
height = int(input("Enter your height in cm :- "))
if height > 120:
    print("You can ride the roller coster")
    bill = 0
    age = int(input("Enter your age to check the prizes "))
    if age < 12:
        bill = 5
    elif 12 < age < 18:  # or we can write that as age>12 and age<18
        bill = 7
    elif 45 < age and age < 55:
        bill = 0
    else:
        bill = 10
    poster = input("You want a poster ? Y or N ")
    if(poster == "Y"):
        bill +=3
        print(f"You have to pay {bill}")
    else:
        print(f"You have to pay {bill}")
else:
    print("You cann't ride the roller coster")

'''
# Challenge no 1

'''
num = int(input("Enter the number you want to check "))
if num % 2 == 0:
    print("This is an Even Number")
else:
    print("This is an Odd Number")
'''

# Challenge no 2

'''
height = float(input("Enter your height in meters :- "))
weight = float(input("Enter your weight in kg "))
bmi = weight/height**2

if bmi < 15:
    print("You are underweight")
elif 15 <= bmi < 20:
    print("You are Skinny")
elif 20 <= bmi < 25:
    print("You have perfect Body")
elif 25 <= bmi < 30:
    print("You are Chubby")
else:
    print("You are Overweight")
'''

# Challenge no 3

'''
year  = int(input("Enter the year you want to check "))
if year%4==0:
    if(year%100==0):
        if(year%400==0):
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
'''

# Challenge no 4

'''
pizza = input("Enter the Size of the pizza ? S,M or L ")
peproni = input("Do you want peporoni to it ? Y or N ")
cheese = input("Do you want extra cheese to it ? Y or N ")

small = 10
medium  = 15
large = 25

extrapeproni_s = 1
extrapeproni_m = 2
extrapeproni_l = 3

extrachesse = 2


bill = 0

if pizza == 'S':
    bill = small
    if peproni == 'Y':
        bill += extrapeproni_s

elif pizza == 'M':
    bill = medium
    if peproni == 'Y':
        bill += extrapeproni_m
    
elif pizza == 'L':
    bill = large
    if peproni == 'Y':
        bill += extrapeproni_l

if cheese == 'Y':
        bill += extrachesse

print(f"Your Total bill is {bill}")
'''


# Challenge no 5

'''
name1 = input("Enter your name ")
name2 = input("Enter your partner name ")

combined_name = name1 +name2
lower_name = combined_name.lower()
t = lower_name.count('t')
r = lower_name.count('r')
u = lower_name.count('u')
e = lower_name.count('e')

true = t+r+u+e

l = lower_name.count('l')
o = lower_name.count('o')
v = lower_name.count('v')
e = lower_name.count('e')

love = l+o+v+e

print(f"Your love is {true}{love}% strong")
'''

