#!/usr/bin/python3
"""This a simple code for the game of hide the money"""
# List containing the characters.
row1 = ['😡', '😡', '😡']
row2 = ['😡', '😡', '😡']
row3 = ['😡', '😡', '😡']

matrix = [row1, row2, row3]  # created a matrix to help in hiding the money

print(f"{row1}\n {row2}\n {row3}")
position = input("Enter the position you want to hide our money:")  # accepting input from the player

row_number = int(position[0])  # This line extracts the first element (character) from the position variable
# and converts it to an integer. This integer is assumed to represent the row number in the matrix

column_number = int(position[1])  # This line extracts the second element (character) from the position variable
# and converts it to an integer. This integer is assumed to represent the column number in the matrix

row_selected = matrix[row_number - 1]  # This line accesses the row in the matrix based on the row_number.
# Since Python uses 0-based indexing for lists, it subtracts 1 from row_number to get the correct index

row_selected[column_number-1] = 'X'  # This line accesses the element within the selected row based on
# the column_number. It sets this element to 'X', effectively marking it as 'X' in the matrix.

print(f"{row1}\n {row2}\n {row3}")  # Print output of the game.
