#!/usr/bin/python3
"""This code simply checks using a simple formula to see if you and your loved one are soulmates or not"""

name1 = input("What is your name? ")  # Input function: Accepting the names of the users
name2 = input("What is his/her name? ")
combine_name = name1 + name2  # This concatenate the two names of the users and stores it in a variable.
lower_case_string = combine_name.lower()  # This makes any name collected from the user into lower case.

# using the .count function to count the number of times the specified strings occurs
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e  # add the scores.

L = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
Love = L + o + v + e  # add the scores.

Love_score = int(str(true) + str(Love))  # this turns the scores into integers and add them

# Condition to check if you and your loved one are soulmates
if Love_score <= 30:
    print(f"Your love score is {Love_score} and you don't belong together")
elif 30 < Love_score <= 70:
    print(f"Your love score is {Love_score}  and you are alright together")
else:
    print(f"Your love score is {Love_score} and you have found your soul mate")
