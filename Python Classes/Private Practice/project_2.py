#Advanced Rock-Paper-Scissors game

import random

def play():
    options = ['rock', 'paper', 'scissors']
    computer = random.choice(options)
    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in options:
        print("Invalid choice. Try again.")
        return

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# Run the game
play()
