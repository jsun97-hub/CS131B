'''
Write a sentinel loop that repeatedly prompts the user to enter a number and, once the number −1 is typed, displays the maximum and minimum numbers that the user entered.

Here is a sample dialogue:

Type a number (or -1 to stop): 5
Type a number (or -1 to stop): 2
Type a number (or -1 to stop): 17
Type a number (or -1 to stop): 8
Type a number (or -1 to stop): -1
Maximum was 17
Minimum was 2
'''

# Initialize variables.
sentinal_value = -1
prompt = "Type a number (or", sentinal_value, "to stop): "
user_input = int(input(prompt))

# Prime the reading.
if user_input == sentinal_value:
    print("No valid numbers were entered.")
else:
    maximum_input = user_input
    minimum_input = user_input

    # Execute sentinal loop.
    while user_input != sentinal_value:
        if user_input > maximum_input:
            maximum_input = user_input
        if user_input < minimum_input:
            minimum_input = user_input
    
        # Obtain input fot the next iteration.
        user_input = int(input(prompt))

    # Print result statements.
    print("Maximum was", maximum_input)
    print("Minimum was", minimum_input)

'''
--------------------------- Sample Run ---------------------------
('Type a number (or', -1, 'to stop): ')-1
No valid numbers were entered.

('Type a number (or', -1, 'to stop): ')-4
('Type a number (or', -1, 'to stop): ')8
('Type a number (or', -1, 'to stop): ')22
('Type a number (or', -1, 'to stop): ')-1
Maximum was 22
Minimum was -4
------------------------- End Sample Run -------------------------
'''