#!/usr/bin/python3
"""This simple code is used to automize the ordering of pizza and showing the bill"""
size = (input("What size of Pizza do you want(S/M/L)? ")).lower()  # Inputs from the user

bill = 0
# condition statements to check if pizza is S/M/L and telling you its appropriate bill.
if size == "s" or size == "S":
    bill += 100
    print("Small size pizza is 100GHC")
elif size == "m" or size == "M":
    bill += 200
    print("Medium size pizza is 200GHC")
else:
    bill += 300
    print("Large size pizza is 300GHC")

# condition statement to see if you wand pepperoni or extra cheese and its appropriate bill
add_peperoni = (input("Do yo want peperoni (Y/N)? "))
if add_peperoni == 'y' or add_peperoni == "Y":
    if size == "s" or size == "S":
        bill += 20
    else:
        bill += 30

extra_cheese = (input("Do you wnt extra cheese (Y/N)? "))
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 15

print(f"Your Total Bill is {bill}GHC")  # Printing the total bill.
