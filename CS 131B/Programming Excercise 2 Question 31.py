'''
Programming Excercise 2 Question 31
Written by Jeffrey Sun on 06/09/2025

Description:
Develop a sentinel-controlled-repetition script that prompts the user to input the miles driven and gallons used for
each tankful. The script should calculate and display the miles per gallon obtained for each tankful.
'''

# Initialize variables.
sentinal_value = -1
prompt_gallons = "Enter the gallons used (-1 to end): "
prompt_miles = "Enter the miles driven: "
gallons_input = float(input(prompt_gallons))

# Prime the reading.
if gallons_input == -1:
    print("No valid numbers were entered.")
else:
    miles_input = float(input(prompt_miles))
    gallons_total = gallons_input
    miles_total = miles_input
    # Print gas mileage statement.
    print("The miles/gallon for this tank was", f'{miles_input / gallons_input:.6f}')

    # Execute sentinal loop
    while gallons_input != sentinal_value:
        print("\n")
        gallons_input = float(input(prompt_gallons))
        if gallons_input == -1:
            break
        miles_input = float(input(prompt_miles))
        # Print gas mileage statement.
        print("The miles/gallon for this tank was", f'{miles_input / gallons_input:.6f}')
        # Update accumulators.
        gallons_total += gallons_input
        miles_total += miles_input

    # Print result statement.
    print("The overall average miles/gallon was", f'{miles_total / gallons_total:.6f}')

'''
------------------------ SAMPLE RUN 1 ------------------------
Enter the gallons used (-1 to end): 12.8
Enter the miles driven: 287
The miles/gallon for this tank was 22.421875


Enter the gallons used (-1 to end): 10.3
Enter the miles driven: 200
The miles/gallon for this tank was 19.417476


Enter the gallons used (-1 to end): 5
Enter the miles driven: 120
The miles/gallon for this tank was 24.000000


Enter the gallons used (-1 to end): -1
The overall average miles/gallon was 21.601423
--------------------- END SAMPLE RUN 1 -----------------------

------------------------ SAMPLE RUN 2 ------------------------
Enter the gallons used (-1 to end): -1
No valid numbers were entered.
--------------------- END SAMPLE RUN 2 -----------------------
'''