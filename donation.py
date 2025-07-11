'''
Program: donation.py. 
Programmer: Jeffrey Sun
Date: 06/24/2025
Description: This program calculates the average pints of blood donated during a blood drive
by taking in the number of pints donated during the drive, based on a seven hour drive period.
The average pints donated during that period should be calculated and displayed. Additionally,
the highest and the lowest number of pints donated should be determined and displayed.  
'''
# Define length of drive as a constant variable
drive_length = 7

# Create main function.
def main():
    '''
    Main function which when executed achieves the items mentioned in the "Description".
    Input: none.
    Output: displays the average, highest, and lowest pints from the blood drive.
    '''
    again = "no"
    while again.lower() == "no":    # Use .lower() method to address case sensitivity
        # Initialize variables.
        pints = []
        total_pints = 0
        average_pints = 0
        high_pints = 0
        low_pints = 0

        # Call functions.
        get_pints(pints)
        total_pints = get_total(pints, total_pints)
        average_pints = get_average(total_pints, average_pints)
        high_pints = get_high(pints, high_pints)
        low_pints = get_low(pints, low_pints)
        display_results(average_pints, high_pints, low_pints)
        again = input("\nDo you want to end program? (Enter no or yes): ")

# Define functions.
def get_pints(pints):
    '''
    Prompts user to enter the pints collected during each hour of the blood drive.
    Input: empty pint list.
    Output: pint list filled with user inputs.
    '''
    for counter in range(drive_length):
        pints.append(int(input("Enter pints collected: ")))
    return pints

def get_total(pints, total_pints):
    '''
    Calculates the total number of pints collected from a blood drive.
    Input: pint list filled with user inputs, initialized total pints variable.
    Output: total number of pints.
    '''
    for item in pints:
        total_pints += item
    return total_pints

def get_average(total_pints, average_pints):
    '''
    Calculates the average number of pints collected per hour from a blood drive.
    Input: total number of pints, initialized average pints variable.
    Output: average number of pints
    '''
    average_pints = total_pints / drive_length
    return average_pints

def get_high(pints, high_pints):
    '''
    Calculates the highest number of pints collected from a single hour during a blood drive.
    Input: pints list, initialized highest pints variable.
    Output: highest number of pints.
    '''
    high_pints = pints[0]
    for item in pints:
        if item > high_pints:
            high_pints = item
    return high_pints

def get_low(pints, low_pints):
    '''
    Calculates the lowest number of pints collected from a single hour during a blood drive.
    Input: pints list, initialized lowest pints variable.
    Output: lowest number of pints.
    '''
    low_pints = pints[0]
    for item in pints:
        if item < low_pints:
            low_pints = item
    return low_pints

def display_results(average_pints, high_pints, low_pints):
    '''
    Displays the average, highest, and lowest number of pints.
    Input: average, highest, and lowest pints.
    Output: prints the average, highest, and lowest number of pints.
    '''
    print("\nThe average number of pints donated is ", average_pints, ".", sep="")
    print("\nThe highest pints donated is ", high_pints, ".", sep="")
    print("\nThe lowest pints donated is ", low_pints, ".", sep="")

# Call main function.
main()

'''
------------Sample Run------------
Enter pints collected: 43
Enter pints collected: 25
Enter pints collected: 64
Enter pints collected: 35
Enter pints collected: 19
Enter pints collected: 37
Enter pints collected: 46

The average number of pints donated is 38.42857142857143.

The highest pints donated is 64.

The lowest pints donated is 19.

Do you want to end program? (Enter no or yes): yes
----------End Sample Run----------
'''