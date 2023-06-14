import random



print(
    '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
    '''
)
words = ["camel", "avagardo", "mansion", "gamer"]

choosen_word = random.choice(words)



pics = ["""
      _______
     |/      |
     |      (_)
     |      \|/
     |     ._|_.  
     |     |   |
     |
    _|___
""","""
      _______
     |/      |
     |      (_)
     |      \|/
     |     ._|  
     |     |   
     |
    _|___
""","""
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |     
     |
    _|___
""","""
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |     
     |
    _|___
""","""
      _______
     |/      |
     |      (_)
     |       |
     |       
     |     
     |
    _|___
""","""
      _______
     |/      |
     |      (_)
     |    
     |      
     |    
     |
    _|___
""","""
      _______
     |/      |
     |      
     |    
     |      
     |    
     |
    _|___
"""
]

# pics = pics.reverse()
score = []
for i in choosen_word:
    score.append("_")

length = len(choosen_word)
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Enter the letter ").lower()
    if guess in score:
        print(f"You already Guess letter {guess}, Please Guess another Letter")
    for num in range(0, length):
        if guess == choosen_word[num]:
            score[num] = guess
        else:
            continue
    print(score)
    if guess not in choosen_word:
        lives -= 1
        print(f"You Guess letter {guess}, That is not in the word")
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"You Guess letter {guess}")
    print(f"Your Lives remains {lives}")
    
    if "_" not in score:
        end_of_game = True
        print("You won")
    print(pics[lives])


