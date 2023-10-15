#!/usr/bin/python3
"""This code  is a similar code to the other code but this time around it accepts the users favourite
name or Word and add random numbers and symbols to it"""
import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['%', '&', '#', '$', '!', '*']

print("Welcome to Password Generator")
words = (input("Input your Favorite Word or Name:\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your password?\n"))


password_list = [words]  # This List contains the inputs of the user and later add symbols and number to it.
for i in range(1, n_numbers + 1):
    nums = random.choice(numbers)
password_list += nums
for i in range(1, n_symbols + 1):
    syms = random.choice(symbols)
password_list += syms

password = " "
for i in password_list:
    password += i
print(password)
