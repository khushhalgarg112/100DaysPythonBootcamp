import random

"""items = ['House','Flat','Bunglow','Farm House']
for item in items:
    print(item)"""

# Challenge no 1

"""height = input("Enter list of students height by spacing ").split(" ")
count = len(height)
num = 0
for i in height:
    num += int(i)

avg = num/count

print(f"The average height is {round(avg)}")"""

# Challenfge no 2

"""marks = input("Enter the marks of the whole class by spacing ").split()
count = len(marks)  # ValueError: invalid literal for int() with base 10: 
# if you give extra space after splliting with spacing but if you use only split() then this error gone 
maximum = 0
for i in range(0, count):
    marks[i] = int(marks[i])

for j in marks:
    if(j > maximum):
        maximum = j
    else:      
        continue

print(f"Maximum marks in the class is {maximum}")"""


# Challenge no 3

"""count = 0
for i in range(0, 101):
    if i % 2 == 0:
        count += i

print(count)"""

# Challenge no 4

"""a = 'Fizz'
b = 'Buzz'
for i in range(1,20):
    if i%3 ==0 and i%5 == 0:
        print(a + b)
    elif i%3 == 0:
        print(a)
    elif i%5 == 0:
        print(b)
    else:
        print(i)
"""

# Password Generator

a = " a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letters = a.split(" ")
b = "1 2 3 4 5 6 7 8 9 0"
numbers = b.split(" ")
c = "! @ # $ % ^ & * ( ) _"
characters = c.split(" ")

no_of_letter = int(input("Enter the number of letters you want in your password:- "))
no_of_number = int(input("Enter the number of numbers you want in your password:- "))
no_of_characters = int(input("Enter the number of characters you want in your password:- "))

'''password = ""         #Easy
for i in range(0,no_of_letter):
    password += random.choice(letters)

for j in range(0,no_of_number):
    password += random.choice(numbers)

for k in range(0,no_of_characters):
    password += random.choice(characters)
'''

password_list = []
for i in range(0,no_of_letter):
    password_list.append(random.choice(letters))

for j in range(0,no_of_number):
    password_list.append(random.choice(numbers))

for k in range(0,no_of_characters):
    password_list.append(random.choice(characters))

random.shuffle(password_list)

password =""

count = len(password_list)
for x in range(0,count):
    password += password_list[x]

print(password)