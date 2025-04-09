#Quiz Game

import tkinter as tk
import random

# Sample question bank (duplicates removed)
jls_extract_var = {"question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "HighText Transport Protocol", "Hyper Transfer Text Protocol", "High Transfer Protocol"], "answer": "HyperText Transfer Protocol"}
question_bank = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Who invented Python?", "options": ["Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "James Gosling"], "answer": "Guido van Rossum"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "Which language is used for web development?", "options": ["Python", "Java", "C", "JavaScript"], "answer": "JavaScript"},
    {"question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "HighText Transport Protocol", "Hyper Transfer Text Protocol", "High Transfer Protocol"], "answer": "HyperText Transfer Protocol"},
    {"question": "What is the full form of CPU?", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit", "Computer Processing Unit"], "answer": "Central Processing Unit"},
    {"question": "Which programming language is used for Android development?", "options": ["Python", "Java", "C++", "Swift"], "answer": "Java"},
    {"question": "What is the full form of CPU?", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit", "Computer Processing Unit"], "answer": "Central Processing Unit"},
    {"question": "Which programming language is used for Android development?", "options": ["Python", "Java", "C++", "Swift"], "answer": "Java"},
    {"question": "Who was the first president of the United States?", "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "answer": "George Washington"},
    {"question": "In which year did World War II end?", "options": ["1945", "1939", "1950", "1920"], "answer": "1945"},
    {"question": "Which country was the first to land a man on the moon?", "options": ["USA", "Soviet Union", "China", "India"], "answer": "USA"},
    {"question": "Who was the first emperor of China?", "options": ["Qin Shi Huang", "Kublai Khan", "Mao Zedong", "Sun Yat-sen"], "answer": "Qin Shi Huang"},
    {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": "Au"}
]

# Initialize global variables
score = 0
current_question = 0

# Function to update the question and options
def next_question():
    global current_question
    question_data = random.choice(question_bank)
    
    # Update the question and options
    question_label.config(text=question_data["question"])
    option1.config(text=question_data["options"][0], command=lambda: check_answer(question_data["options"][0], question_data["answer"]))
    option2.config(text=question_data["options"][1], command=lambda: check_answer(question_data["options"][1], question_data["answer"]))
    option3.config(text=question_data["options"][2], command=lambda: check_answer(question_data["options"][2], question_data["answer"]))
    option4.config(text=question_data["options"][3], command=lambda: check_answer(question_data["options"][3], question_data["answer"]))

# Function to check the player's answer
def check_answer(player_choice, correct_answer):
    global score
    if player_choice == correct_answer:
        score += 1
    score_label.config(text=f"Score: {score}")
    next_question()

# Function to start the quiz
def start_quiz():
    global score, current_question
    score = 0
    current_question = 0
    score_label.config(text=f"Score: {score}")
    next_question()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x400")

# Title label
title_label = tk.Label(root, text="Quiz App", font=("Arial", 20))
title_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=5)

# Question label
question_label = tk.Label(root, text="Welcome to the quiz!", font=("Arial", 14), wraplength=350)
question_label.pack(pady=20)

# Buttons for options
option1 = tk.Button(root, text="Option 1", width=20, height=2)
option1.pack(pady=5)

option2 = tk.Button(root, text="Option 2", width=20, height=2)
option2.pack(pady=5)

option3 = tk.Button(root, text="Option 3", width=20, height=2)
option3.pack(pady=5)

option4 = tk.Button(root, text="Option 4", width=20, height=2)
option4.pack(pady=5)

# Start button
start_btn = tk.Button(root, text="Start Quiz", width=20, height=2, command=start_quiz)
start_btn.pack(pady=20)

# Run the app
root.mainloop()
