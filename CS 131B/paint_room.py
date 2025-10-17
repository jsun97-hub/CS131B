"""
Program: paint_room.py
Programmer: Jeffrey Sun
Class: CS 131B Summer 2025
Date: 06/4/2024
Description: The program calculates the amount of paint needed to paint the walls of a room of the given length and
width. It assumes that the paint covers 350 square feet per gallon.
"""
import math # Import math library for the ceiling rounding

# Declare constants.
COVERAGE = 350  # Paint covers 350 sq ft/gal.
DOOR_AREA = 20  # Door area in square ft.
WINDOW_AREA = 15    # Window area in square ft.

# Prompt user for other input variables and convert inputs into int data type.
length = int(input("Enter the length of the room: "))
width = int(input("Enter the width of the room: "))
height = int(input("Enter the height of the room: "))
num_doors = int(input("How many doors are in the room? "))
num_windows = int(input("How many windows are in the room? "))

# Calculate the amount of paint needed.
total_sqft = 2 * width * height + 2 * length * height
total_sqft  = total_sqft - num_doors * DOOR_AREA - num_windows * WINDOW_AREA    # Re-calculate after accounting for doors and windows.
paint_needed = total_sqft  / COVERAGE


# Print the input information and credits left.
print(f'{paint_needed:.2f}', "gallon(s) of paint are needed to paint a room", width, "feet wide by", length,
      "feet long by", height, "feet high with", num_doors, "doors and", num_windows, "windows.")

""" 
------------------------- Sample Run -------------------------------------------------------------------------------------
Enter the length of the room: 15
Enter the width of the room: 12
Enter the height of the room: 8
How many doors are in the room? 1
How many windows are in the room? 2
1.09 gallon(s) of paint are needed to paint a room 12 feet wide by 15 feet long by 8 feet high with 1 doors and 2 windows.
------------------------- End Sample Run ---------------------------------------------------------------------------------
""" 