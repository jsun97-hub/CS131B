'''
CS 131B Project 13
I promise that I understand the code I am submitting well enough to write similar code on a test.
'''
'''
Program:  building_numbers.py. 
Programmer: Jeffrey Sun
Date: 07/25/2025
Description: This program keeps track of who works in what building.
Each person will be identified by their first name, and each building 
will be identified by a number. While the program is running, this 
information will be stored in a dictionary. When the program is not 
running, the information will be kept in a file.
'''
# Part 2 - DictionaryFileManager Class
class DictionaryFileManager:
    '''
    constructor: __init__(self, filename)
    filename: "dictionary.txt"
    '''
    def __init__ (self, filename):
        self.filename = filename
    
    def write_dictionary_to_file(self, dictionary):
        '''
        parameter: dictionary
        dictionary: for this project, building_numbers
        '''
        with open(self.filename, "w") as f:
            for k, v in dictionary.items():
                f.write(f"{k} {v}\n")

    def read_dictionary_from_file(self):
        '''
        return value: dictionary
        dictionary: for this projectm building_numbers
        '''
        try:
            with open(self.filename, "r") as f:
                dictionary = {}
                for line in f:
                    k, v = line.strip().split()
                    dictionary[k] = int(v)
                return dictionary
        except FileNotFoundError:
            return {}
    
# Part 1 + 3 - User Interaction + Use Your DictionaryFileManager Class
def main():
    manager = DictionaryFileManager("dictionary.txt")

    building_numbers = manager.read_dictionary_from_file()

    name = input("Enter new name: ")

    if name != "":
        building_number = int(input("Enter building number: "))
        building_numbers[name] = building_number

    lookup_name = input("Enter name to look up: ")

    if lookup_name in building_numbers:
        print(lookup_name, "is in Building", building_numbers[lookup_name])

    manager.write_dictionary_to_file(building_numbers)

# Call the main function.
main()
'''
--------------Sample Output--------------
PS C:\Users\jsun\OneDrive - Amyris\Documents\CS\CS 131B> & "C:/Program Files/Python313/python.exe" "c:/Users/jsun/OneDrive - Amyris/Documents/CS/CS 131B/building_numbers.py"
Enter new name: Jeffrey
Enter building number: 22
Enter name to look up: Jeffrey
Jeffrey is in Building 22
PS C:\Users\jsun\OneDrive - Amyris\Documents\CS\CS 131B> & "C:/Program Files/Python313/python.exe" "c:/Users/jsun/OneDrive - Amyris/Documents/CS/CS 131B/building_numbers.py"
Enter new name: Hanan
Enter building number: 100
Enter name to look up: Jeffrey
Jeffrey is in Building 22
PS C:\Users\jsun\OneDrive - Amyris\Documents\CS\CS 131B> & "C:/Program Files/Python313/python.exe" "c:/Users/jsun/OneDrive - Amyris/Documents/CS/CS 131B/building_numbers.py"
Enter new name: Michael Jordan
Enter building number: 23
Enter name to look up: Hanan
Hanan is in Building 100
------------End Sample Output------------
'''