'''
Program: schedule.py
Programmer: Jeffrey Sun
Class: CS 131B Summer 2025
Date: 07/07/2025
Description: CS 131B Project 6. This program defines a round robin scheduling function.
'''
# Define round robin function.
def generate_round_robin_schedule(a_list):
    '''
    Round robin scheduling function.

    Parameters: a list of strings (names).

    Return value(s): a list of tuples (pairs of students).
    '''
    # Create a shallow copy of the input list.
    list_copy = list(a_list)

    # Add a "bye" if a_list has an odd number of elements
    if len(list_copy) % 2 != 0:
        list_copy.append("bye")

    # Initialize other utility variables.
    n = len(list_copy)
    schedule = []

    # Use nested for-loop to iterate through the list.
    for round in range (n - 1):
        round_pairs = []
        for i in range(n // 2):
            round_pairs.append((list_copy[i], list_copy[n - 1 - i]))

        schedule.extend(round_pairs)
        list_copy = [list_copy[0]] + [list_copy[-1]] + list_copy[1:-1]

    # Return new list of pairs.
    return schedule

# Define main function.
def main():
    pairs = (generate_round_robin_schedule(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))
    print(pairs)

# Run main function.
main()

'''
------------------------ Sample Output ------------------------
[('A', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E'), ('A', 'G'), ('H', 'F'), ('B', 'E'), 
('C', 'D'), ('A', 'F'), ('G', 'E'), ('H', 'D'), ('B', 'C'), ('A', 'E'), ('F', 'D'), 
('G', 'C'), ('H', 'B'), ('A', 'D'), ('E', 'C'), ('F', 'B'), ('G', 'H'), ('A', 'C'), 
('D', 'B'), ('E', 'H'), ('F', 'G'), ('A', 'B'), ('C', 'H'), ('D', 'G'), ('E', 'F')]
---------------------- End Sample Output ----------------------
'''
