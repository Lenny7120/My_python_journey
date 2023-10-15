#!/usr/bin/python3
"""This is a simple code for the Hangman Game"""
# Imported these modules, created two of them(Hangman_stages and Word_file)
import random
import Hangman_stages
import Word_file

chosen_word = random.choice(Word_file.words)  # Used the random.choice to chose random words I wrote in Word files
# Printing to the standard output.
print("Let's Play Hangman Game")
print("You have six(6) lives, so attempt to guess in six(6) tries good luck !")
lives = 6  # Number of lives to be lost.
display = []  # Created an empty list to be filled later.
# Iterating the random chosen word to display the '_____" of the word for the player to guess it
for word in range(len(chosen_word)):
    display += '_'
print(display)

Game_over = False  # Used this condition for the game to continually run until you lose or win.
while not Game_over:
    guessed_letter = input("Guess a Letter: ").lower()  # Accepting the input of the player.
# Iterating through chosen to find if the guessed word is correct.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
# condition if guessed word is wrong
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            Game_over = True
            print(chosen_word)  # To print the correct word when you lose so u can know the answer
            print("You Lose!!")
# Condition if you are able to guess all the words correctly.
    if '_' not in display:
        Game_over = True
        print("You Win!!")
    print(Hangman_stages.stages[lives])  # To Print the hangman images.
