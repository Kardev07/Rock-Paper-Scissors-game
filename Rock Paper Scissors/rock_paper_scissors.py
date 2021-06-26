import random

def play():
    user = input("What is your choice? Enter 'r' for Rock, 'p' for Paper and 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie!'

    if win(user,computer):
        return 'You Win!'

    return 'You Lost! Try again'

def win(player, oppenent):
    if(player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p') or (player == 'p' and oppenent == 'r'):
        return True

print(play())