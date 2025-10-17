'''
Program:  recursivepalindrome.py 
Programmer: Jeffrey Sun
Date: 07/23/2025
Description: This program uses recursion to identify if an immutable input is
a palindrome.
'''
def isPalindrome(object):
    # Define base cases. 
    # If the object is 1 or 0 elements, than it is a palindrome.
    if len(object) < 2:
        return True
    # If the object is of even length, than it cannot be a palindrome.
    elif len(object) % 2 == 0:
        return False
    # Define recursive case. 
    else:
        # If the object's first and last elements are equal,
        if object[0] == object[-1]:
            # recursively call the function excluding the first and last elements of the original input.
            return isPalindrome(object[1:-1])
        else:
            return False
        
def main():
    input1 = (1, 2, 3, 2, 1)
    input2 = (1, 2, 3, 4, 5)
    input3 = "racecar"
    input4 = "hello"
    input5 = ("r","a","c","e","c","a","r")

    results = [isPalindrome(input1), isPalindrome(input2), isPalindrome(input3), isPalindrome(input4), isPalindrome(input5)]

    return print((results, isPalindrome(results)))

main()

'''
---------------Sample Output---------------
([True, False, True, False, True], True)
-------------End Sample Output-------------
'''