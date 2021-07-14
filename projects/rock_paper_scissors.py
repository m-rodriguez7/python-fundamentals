import random

def get_user_selection():
    action = int(input("Enter a choice (0 = scissor, 1 = rock, 2 = paper): "))
    while action > 2 or action < 0:
        print("Invalid Number")
        action = int(input("Enter a choice (0 = scissor, 1 = rock, 2 = paper): "))
    
    hand = get_hand(action)
    return hand

def get_computer_selection():
    action = random.randint(0,2)
    hand = get_hand(action)
    return hand

def get_hand(hand):
    str = ''
    if (hand == 0):
        str = 'scissor'
    elif (hand == 1):
        str = 'rock'
    elif (hand == 2):
        str = 'paper'
    else:
        str = hand
    return str

def determine_winner(userHand,computerHand):
    winner = ""
    if (userHand == computerHand):
        return "tie"
    elif (userHand == "scissor" and computerHand == "paper"):
        winner = "user"
    elif (userHand == "rock" and computerHand == "scissor"):
        winner = "user"
    elif (userHand == "paper" and computerHand == "rock"):
        winner = "user"
    else:
        winner = "computer"
    return winner

print("Rock, Paper, Scissor Game")

while True:
    try:
        user_hand = get_user_selection()
        print(f"User Hand: {user_hand}")
    except ValueError as err:
        print("Only a numbers 0, 1, or 2 is accepted")
        continue
    
    computer_hand = get_computer_selection()
    print(f"Computer Hand: {computer_hand}")

    winner = determine_winner(user_hand,computer_hand)

    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f"The winner is: {winner}")
        break

