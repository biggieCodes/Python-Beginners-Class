# Rock Paper Scissors GAME

import tkinter as tk
import random

# Global variables
player_score = 0
computer_score = 0
player_name = ""

# Get computer choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Determine winner
def determine_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'player'
    else:
        return 'computer'

# Game logic
def play(player_choice):
    global player_score, computer_score, player_name

    computer_choice = get_computer_choice()
    winner = determine_winner(player_choice, computer_choice)

    result_text = f"{player_name} chose {player_choice}\nComputer chose {computer_choice}\n"

    if winner == 'player':
        player_score += 1
        result_text += f"{player_name} wins this round!"
    elif winner == 'computer':
        computer_score += 1
        result_text += "Computer wins this round!"
    else:
        result_text += "It's a tie!"

    result_label.config(text=result_text)
    score_label.config(text=f"{player_name}: {player_score}  |  Computer: {computer_score}")

    if player_score == 3 or computer_score == 3:
        final_result = f"🎉 {player_name} wins the game!" if player_score == 3 else "😓 Computer wins the game!"
        result_label.config(text=final_result)
        disable_buttons()

# Disable choice buttons
def disable_buttons():
    rock_btn.config(state=tk.DISABLED)
    paper_btn.config(state=tk.DISABLED)
    scissors_btn.config(state=tk.DISABLED)

# Reset game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text=f"{player_name}: 0  |  Computer: 0")
    result_label.config(text="Choose rock, paper, or scissors")
    rock_btn.config(state=tk.NORMAL)
    paper_btn.config(state=tk.NORMAL)
    scissors_btn.config(state=tk.NORMAL)

# Start game after entering name
def start_game():
    global player_name
    player_name = name_entry.get().strip()
    if player_name == "":
        result_label.config(text="Please enter your name to start.")
        return

    name_frame.pack_forget()
    game_frame.pack()
    result_label.config(text="Choose rock, paper, or scissors")
    score_label.config(text=f"{player_name}: 0  |  Computer: 0")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x450")

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(pady=10)

# Frame for name input
name_frame = tk.Frame(root)
name_label = tk.Label(name_frame, text="Enter your name:", font=("Arial", 12))
name_label.pack(pady=5)
name_entry = tk.Entry(name_frame, font=("Arial", 12))
name_entry.pack(pady=5)
start_btn = tk.Button(name_frame, text="Start Game", command=start_game)
start_btn.pack(pady=10)
name_frame.pack(pady=20)

# Frame for the actual game (initially hidden)
game_frame = tk.Frame(root)

score_label = tk.Label(game_frame, text="You: 0  |  Computer: 0", font=("Arial", 14))
score_label.pack(pady=5)

result_label = tk.Label(game_frame, text="", font=("Arial", 12), wraplength=300)
result_label.pack(pady=20)

rock_btn = tk.Button(game_frame, text="Rock", width=10, height=2, command=lambda: play("rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(game_frame, text="Paper", width=10, height=2, command=lambda: play("paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(game_frame, text="Scissors", width=10, height=2, command=lambda: play("scissors"))
scissors_btn.pack(pady=5)

reset_btn = tk.Button(game_frame, text="Reset Game", width=15, height=2, command=reset_game)
reset_btn.pack(pady=20)

# Run app
root.mainloop()
