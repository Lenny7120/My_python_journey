#!/usr/bin/python3
"""This is a simple code for a Rock Paper Scissors Game"""
import random  # Imported a random module to randomize the computer's choice
user_choice = int(input("Enter your Choice: 0 for Rock, 1 for Paper, 2 for Scissors: "))  # Accepting player's input
if user_choice > 2:  # condition to make sure players don't chose numbers  not stated
    print("Wrong input, You lose")
else:
    computer_choice = random.randint(0, 2)  # Random module to randomize computer's choice.

    print("Computer Choice: ", end=" ")
    print(computer_choice)  # printing computer's random choice
# conditions for the various outcome of the game
    if computer_choice == user_choice:
        print("It's a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You win.")
