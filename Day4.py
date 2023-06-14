import random

# Challenge no 1
'''
while True:
    seeds = int(input("Enter your seed number"))
    random.seed(seeds)
    # print(random.choice(['Head', "Tail"]))

    num = random.randint(0,1)
    if num ==0:
        print("Heads")
    else:
        print("Tails")
'''

# Challenge no 2

'''
names = input("Enter the name of every member :- ")
name_list = names.split(" ")
count  = len(name_list)
num = random.randint(0,count-1)
print(f"{name_list[num]} is going to buy meal today.")
'''

# Challenge no 3

'''row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
row = [row1, row2, row3]

treasure = input("Enter the location where you put your tresure:- ")
row[int(treasure[0])][int(treasure[1])] = 'x'

print(f"{row[0]}\n{row[1]}\n{row[2]}")
'''


# Rock,Paper&Scissor game

while True:
    choose = int(input("Type 0 for Rock , 1 for Paper , 2 for Scissor:- "))

    if choose < 3:
        if choose == 0:
            print('''
        you choose
               ___..__
      __..--""" ._ __.'
                  "-..
                '"--..)
     ___        '--...)
        `-..__ '"--...)
              """"----'    
        ''')
        elif choose == 1:
            print('''
            you choose
                _
            _  / |  __  
           / \ | | / /__
            \ \| |/ // /  
             \ Y | // /
           .-.) '. `_/
          (.-.   / /
              | ' |
              |___|
             [_____]
             |     |
            ''')
        elif choose == 2:
            print('''
            you choose
          .-.  _
          | | / )
          | |/ /
         _|__ /_
        / __)-' )
        \  `(.-')
        >_._>-'
        /  /

            ''')

        computer = random.randint(0, 2)
        if computer == 0:
            print('''
            computer choose
                ___..__
        __..--""" ._ __.'
                    "-..
                    '"--.)
        ___        '--...)
            `-..__ '"--...)
                """"----'     
            ''')
        elif computer == 1:
            print('''
            computer choose
                _
            _  / |  __  
           / \ | | / /__
            \ \| |/ // /  
             \ Y | // /
           .-.) '. `_/
          (.-.   / /
              | ' |
              |___|
             [_____]
             |     |
            ''')
        elif computer == 2:
            print('''
            computer choose
          .-.  _
          | | / )
          | |/ /
         _|__ /_
        / __)-' )
        \  `(.-')
        >_._>-'
        /  /
            ''')

        print("\n")

        if choose == computer:
            print("Game is Tie")
        else:
            if choose == 0 and computer == 1:
                print("Computer Wins")
            elif choose == 1 and computer == 0:
                print("You Wins")
            elif choose == 0 and computer == 2:
                print("You Wins")
            elif choose == 1 and computer == 2:
                print("Computer Wins")
            elif choose == 2 and computer == 0:
                print("Computer Wins")
            elif choose == 2 and computer == 1:
                print("You Wins")

        print("\n")
    else:
        print("Invalid input")
        exit()
