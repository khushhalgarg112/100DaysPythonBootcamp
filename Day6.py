'''def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   ''' 
    
#move()
#move()
#turn_left()
#move()
#move()
#turn_right()
#move()
#ove()
#turn_left()
#move()
#move()
#turn_right()
#move()
#move()
#turn_left()
#move()
#move()
#turn_right()
#move()
#move()

'''
move()
move()
turn_left()
move()
move()
turn_left()
move()
move()
turn_left()
move()
move()
turn_left()'''

'''def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while at_goal() != True:
    hurdle()'''

# Challenge

'''
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
        '''


# Challenge
'''
def jump():
    turn_left()
    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
        
'''

# Maze Problem

'''
while at_goal() !=True:
    if right_is_clear():
        turn_right()
        move()
    else front_is_clear():
        move()
    else:
        turn_left()
'''