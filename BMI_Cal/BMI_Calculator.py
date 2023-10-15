#!/usr/bin/python3
""" This contains my very simple code for BMI Calculator"""
print("Welcome to my BMI calculator")
weight = float(input("Your weight in kg: "))  # input function: accepting inputs from the user.
height = float(input("Your height in meters: "))

Bmi = weight / (height ** 2)  # Creating a variable called Bmi and storing the formula for calculating BMI.
print(f"Your BMI is:  {Bmi : .2f}")  # Print function: printing the final score in 2 decimal places.

""" The If Else function to determine if the user is underweight, normal, overweight or obese"""
if Bmi <= 18.4:
    print("You are underweight")
elif 18.5 <= Bmi <= 24.9:
    print("You are normal")
elif 25.0 <= Bmi <= 39.9:
    print("You are overweight")
else:
    print("You are obese")
