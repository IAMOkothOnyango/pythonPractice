'''
Implementation of rock, paper, scissors by Okoth Onyango
Github: https://www.github.com/IAmOkothOnyango
'''
import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # Check if the player wins based on the rock-paper-scissors rules
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r')

print(play())
