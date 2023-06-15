import os
# Multiple return statement
"""def name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't enter any name."

    final = f"{f_name} {l_name}"
    final = final.title()
    return final


first_name = input("Enter your name :- ")
last_name = input("Enter your Surname:- ")

result = name(f_name=first_name, l_name=last_name)
print(result)"""

# Challenge no 1


'''def is_leap(year):
    """Take a number as year and return true if the year is leap or false if not""" 
    # ''' """Docstring give documentation to our code
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    if is_leap(year) and month == 2:
        result = 29
    else:
        result = days[month - 1]

    return result


year = int(input("Enter the year "))
month = int(input("Enter the month number "))
if month > 12:
    print("Invalid month number")
else:
    no_of_days = days_in_month(year, month)
    print(f"Days are {no_of_days}")
"""

# Calculator app before watching the tutorial

"""def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

result =0
end = True
while end:
    num1 = int(input("Enter the first numebr:- "))
    operation = input("Enter the operation you want to do \n+\n-\n*\n/\n")
    num2 = int(input("Enter the second number:- "))
    if operation == "+":
        result = add(num1,num2)
    elif operation == "-":
        result = sub(num1,num2)
    elif operation == "*":
        result = multiply(num1,num2)
    elif operation == "/":
        result = divide(num1,num2)

    print(result)

    stay = input("IF you want to work with this number then Type 'Y' or Type 'N' for restart and 'exit' to exit the program:- ")
    if stay == 'Y':
        end_inside = True
        while end_inside:
            operation = input("Enter the operation you want to do \n+\n-\n*\n/\n")
            num3 = int(input("Enter the number:- "))
            if operation == "+":
                result = add(result,num3)
            elif operation == "-":
                result = sub(result,num3)
            elif operation == "*":
                result = multiply(result,num3)
            elif operation == "/":
                result = divide(result,num3)
            print(result)
            stay1 = input("IF you want to work with this number then Type 'Y' or Type 'N' for restart ")
            if stay1 == 'Y':
                continue
            elif stay1 == 'N':
                end_inside = False
    elif stay == 'N':
        result = 0
    elif stay == "exit":
        end = False"""

# Calculator app after watching tutorial


print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {"+": add, "-": sub, "*": multiply, "/": divide}

def calculator():
    num1 = float(input("Enter the first number-> "))
    for key in operations:
        print(key)
    end = True
    while end:
        operation_sym = input("Choose one operation form the above-> ")
        num2 = float(input("Enter the next number-> "))

        function = operations[operation_sym]
        answer = function(num1, num2)

        print(f"{num1} {operation_sym} {num2} = {answer}")
        cont = input(f"Type y to continue with {answer} or type n to restart-> ")
        if cont == 'y':
            num1 = answer
        else:
            os.system('cls')
            calculator()
        
calculator()