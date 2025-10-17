"""
Discussion Board: Operators and Type Conversion Excerise 2

Programmer: Jeffrey Sun
Class: CS 131B Summer 2025
Date: 06/4/2024
"""

start = float(input('Enter your starting mileage: '))
end = float(input('Enter your ending mileage: '))
gallons = float(input('Enter the gallons used: '))
# Calculate the average miles per gallon.
average = (end - start) / gallons
# Display the average to two decimal places.
print("Your average miles per gallon is:", round(average), "miles per gallon")

"""
------------------- Sample Output -------------------
Enter your starting mileage: 0
Enter your ending mileage: 60
Enter the gallons used: 5
Your average miles per gallon is: 12 miles per gallon
------------------- End Sample Output -------------------
"""