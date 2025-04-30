# A rock, paper, scissors game
# This is a simple rock, paper, scissors game where the user plays against the computer.

import random
import time

options = ["rock", "paper", "scissors"]

win_massage = {
    ("rock", "scissors"): "Rock smashes Scissors!",
    ("paper", "rock"): "Paper covers Rock!",
    ("scissors", "paper"): "Scissors cuts Paper!"
}

while True: 
    user_input = input("Enter a choice (rock, paper, scissors): ").lower()
    computer_input = random.choice(options)

    print("Rock... Paper... Scissors...")
    time.sleep(1)
    print("Rock... Paper... Scissors...")
    time.sleep(1)
    print("Rock... Paper... Scissors...")
    time.sleep(1)
    
    print("")
    print(f"The computer chose: {computer_input}")
    print(f"And you chose: {user_input}")

    if user_input == computer_input:
        print(f"Both players selected {user_input}. It's a tie!")

    elif (user_input, computer_input) in win_massage:
        print(f"{win_massage[(user_input, computer_input)]} You won!!")

    else:
        print(f"{win_massage.get((computer_input, user_input), 'Computer played better!')} Computer wins!")
