"""
Program: student_info.py
Programmer: Jeffrey Sun
Class: CS 131B Summer 2025
Date: 06/4/2024
Description: The program displays student basic information and calculates how many credits are needed to graduate.
"""

# Declare variables to hold user inputs.
student_name = ""                                                   # student_name will represent the user's inputted name
degree_program = ""                                                 # degree_program will represent the user's inputted degree program
credits_degree = ""                                                 # credits_degree will represent the user's inputted number of credits required
credits_taken = ""                                                  # credits_taken will represent the user's inputted number of credits taken

# Obtain user inputs and assign values to the declared variables.
student_name = input("Enter student name: ")
degree_program = input("Enter degree program: ")
credits_degree = input("Enter credits required for degree: ")
credits_taken = input("Enter credits taken so far: ")

# Convert variable types from strings to the appropriate types.
student_name = str(student_name)                                    # Note: variable is already a string, but this line is included to demonstrate type conversion
degree_program = str(degree_program)                                # Note: variable is already a string, but this line is included to demonstrate type conversion
credits_degree = int(credits_degree)
credits_taken = int(credits_taken)

# Calculate the number of credits still needed to graduate.
credits_left = credits_degree - credits_taken                       # This calculation determines the difference between the credits required and the credits taken to determine the number of credits still needed

# Print the input information and credits left
print("\nThe student's name is ", student_name, ".", sep = '')      # Use sep keyword to place punction marks without spaces.
print("The degree program is " , degree_program, ".", sep = '')     # Use sep keyword to place punction marks without spaces.
print("The program requires", credits_degree, "and they have taken", credits_taken, "so far.")
print("This means there are", credits_left, "left to take.") 

""" 
------------------------- Sample Run -------------------------
Enter student name: Alex Williams 
Enter degree program: Computer Programming
Enter credits required for degree: 63
Enter credits taken so far: 26

The student's name is Alex Williams.
The degree program is Computer Programming.
The program requires 63 and they have taken 26 so far.
This means there are 37 left to take.
------------------------- End Sample Run ---------------------
""" 