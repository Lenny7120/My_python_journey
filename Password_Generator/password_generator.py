#!/usr/bin/python3
"""This simple code generates a password for the user"""
import random  # import function: imported a random module to help us randomize the password

# Letters, numbers and symbols provided for the password.
letters = ['a', 'b,' 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['%', '&', '#', '$', '!', '*']

print("Welcome to Password Generator")  # printing to the standard output.

# accepting the input of the users and changing them into integers.
n_letters = int(input("How many letters you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your password?\n"))
password_list = []  # Creating an empty list to be filled later.

# iterating through the information given by the users and choosing random letters, symbols and numbers
# and adding them to the empty list
for i in range(1, n_letters + 1):
    char = random.choice(letters)
    password_list += char
for i in range(1, n_numbers + 1):
    nums = random.choice(numbers)
    password_list += nums
for i in range(1, n_symbols + 1):
    syms = random.choice(symbols)
    password_list += syms
random.shuffle(password_list)  # Shuffling the final password
password = ""  # Creating an empty string called password
for i in password_list: # iterating through the list containing the password and changing them into a string
    password += i
print(password)  # printing the final password.
