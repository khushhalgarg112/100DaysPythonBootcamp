import random
import os


# Code before watching Tutorial
'''def add(list):
    result = 0
    for i in list:
        result += int(i)

    return result

def print_card(player,computer):
    print(f"Your cards {player}")
    print(f"Computer Cards {computer}")

def result(player_total,computer_total):
    if player_total > computer_total and player_total < 21:
        print("You Win")
    elif player_total == computer_total:
        print("Match Draw ")
    elif computer_total > 21:
        print("You Win")
    else:
        print("You Lose ")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
end = True
while end:
    player = []
    computer = []
    player_total = 0
    computer_total = 0
    play = input("Type 'y' to play the game and 'n' to exit the game-> ")
    if play == "y":
        for i in range(0, 2):
            player.append(random.choice(cards))
            computer.append(random.choice(cards))
        print(f"Your cards {player}")
        print(f"One Card of Computer {computer[0]}")
        player_total = add(player)
        computer_total = add(computer)
        pick = input("Type 'y' to pick one card and 'n' to pass-> ")
        if pick == "y":
            player.append(random.choice(cards))
            print_card(player,computer)
            player_total = add(player)
            result(player_total,computer_total)
        elif pick == "n":
            print_card(player,computer)
            result(player_total,computer_total)

    elif play == "n":
        end = False'''


# Code after watching Tutorial

def card():
    """Choose Random number from a deck of card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    return random.choice(cards)

def total(cards):
    """Return total of a list """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score,computer_score):
    if player_score == computer_score:
        print("Its a Draw")
    elif computer_score == 0:
        print("Computer Win with a BlackJack")
    elif player_score == 0:
        print("You Win with a BlackJack")
    elif player_score >21:
        print("You Lose, You went over")
    elif computer_score >21:
        print("You win, opponent went over")
    elif player_score > computer_score:
        print("You Win")
    else:
        print("You lose")

def play_game():

    print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   <
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\|
                       _/ |                
                      |__/                 
    """)
    players_cards =[]
    computer_cards = []
    is_game_over  = False
    for i in range(2):
        players_cards.append(card())
        computer_cards.append(card())

    while not is_game_over:
        player_score = total(players_cards)
        computer_score = total(computer_cards)
        print(f"Your Card is {players_cards}, Your score is {player_score}")
        print(f"One cad of computer is {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score >21:
            is_game_over = True
        else:
            player_input = input("Type 'y' to pick one card and 'n' to pass-> ")
            if player_input == 'y':
                players_cards.append(card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score <17:
        computer_cards.append(card())
        computer_score = total(computer_cards)

    print(f"Your Card is {players_cards}, Your total score is {player_score}")
    print(f"Computer Card is {computer_cards}, Your score is {computer_score}")
    compare(player_score,computer_score)

while input("Type 'y' to play the game and 'n' to exit the game-> ") == 'y':
    os.system('cls')
    play_game()