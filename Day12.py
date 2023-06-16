import random
# global and local varibale 

'''
a = 1 #global varibale

def add():
    a = 2
    return a # local variable  this is different variable from global variable it become global variable if we use 'global' keyword with it
'''

# Global keyword
'''
a = 1 #global varibale

def add():
    # global c  this global keyword only excess global varibale and change them but  not make new global varibable inside a function
    c = 2

print(c)
'''


# Changing global varible without making achange into them

'''def add():
    return a+1


a = 2

print(add())

# if we put a =2 here then it gives us an error because we call add() before assigning a variable a
 
print(a)'''

# global varibale
 
'''pi =321

def prin():
    print(pi)  # we can access global variable  here

prin()'''

# Number Guessing Game

def guessed(attempt,random_number):
    for i in range(0,attempt):
        if i>0:
            print("Guess again")
        choose  = int(input(f"You have {attempt-i} Guesses-> "))
        if choose > random_number:
            print("Too High")
        elif choose < random_number:
            print("Too low")
        else:
            return True
    return False

def result(fun, random_number):
    if fun:
        print(f"You made Correct Guess which is {random_number}")
    else:
        print("You have run out of all guess, YOU LOST!")
        print(f"Correct Number is {random_number}")

print("Welcome to the Number Guessing game!")
print('''
   ___                                              _      _                        _  _                    _                      
  / __|   _  _     ___     ___     ___      o O O  | |_   | |_      ___      o O O | \| |   _  _    _ __   | |__     ___      _ _  
 | (_ |  | +| |   / -_)   (_-<    (_-<     o       |  _|  | ' \    / -_)    o      | .` |  | +| |  | '  \  | '_ \   / -_)    | '_| 
  \___|   \_,_|   \___|   /__/_   /__/_   TS__[O]  _\__|  |_||_|   \___|   TS__[O] |_|\_|   \_,_|  |_|_|_| |_.__/   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
''')
print("Guess the number between 1 to 100")
level = input("Choose the Level of the Game Type 'e' for easy and 'h' for hard-> " )
random_number = random.randint(1,100)
attempt = 0
if level == 'e':
    attempt =10
    result(guessed(attempt,random_number),random_number)
elif level == 'h':
    attempt =5
    result(guessed(attempt,random_number),random_number)


 

          
