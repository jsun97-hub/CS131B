'''
Program:  blog_entry.py 
Programmer: Jeffrey Sun
Date: 06/20/2025
Description: 
'''
# Define constants:
min_user_name_length = 2
min_text_length = 100
max_text_length = 500
key_character_length = 1

# Define helper/auxillary function(s).
def get_length(a_string):
    if type(a_string) != str:
        print("Function requires a valid string.")
    else:
        count = 0
        for character in a_string:
            count += 1
        return count
    
def get_range(an_integer):
    output_range = []
    index = 0
    while index != an_integer:
        output_range += [index]
        index += 1
    return output_range
    
# Define assignment function(s).
def get_user_name():
    correct = False
    while not correct:
        user_name = input("Enter user name: ")
        if get_length(user_name) < min_user_name_length:
            print("\nError: user name must be at least", min_user_name_length, "characters.")
        else:
            correct = True
    return user_name

def get_text():
    correct = False
    while not correct:
        text = input("\nEnter text: ")
        if get_length(text) < min_text_length:
            print("\nError: text must be at least", min_text_length, "characters.")
        elif get_length(text) > max_text_length:
            print("\nError: text must be at most", max_text_length, "characters.")
        else:
            correct = True
    return text

def get_key_character():
    correct = False
    while not correct:
        key_character = input("\nEnter key character: ")
        if get_length(key_character) > key_character_length:
            print("\nError: key character must be", key_character_length, "character.")
        else:
            correct = True
    return key_character

def get_first_ten_words(the_string):
    if type(the_string) != str:
        print("\nFunction requires a valid string.")
    else:
        word_count = 0
        first_ten_words = ""
        previous_space_index = 0
        for i in get_range(get_length(the_string)):
            if word_count >= 10:
                break
            else:
                if the_string[i] == " ":
                    first_ten_words += the_string[previous_space_index:i]
                    previous_space_index = i
                    word_count += 1
        return first_ten_words

def mask_character(the_string, key_character):
    if type(the_string) != str:
        print("\nFunction requires a valid string.")
    elif type(key_character) != str or get_length(key_character) > key_character_length:
        print("\nFunction requires a valid key character.")
    else:
        masked_string = ""
        for char in the_string:
            if char == key_character:
                masked_string += "*"
            else:
                masked_string += char
        return masked_string

def count_key(the_string, key_character):
    count = 0
    for char in the_string:
        if char == key_character:
            count +=1
    return count

# Define main function.
def main():
    # 1) Calls get_user_name() and stores the return value in the variable user_name.
    user_name = get_user_name()

    # 2) Calls get_text() and stores the return value in the variable the_text.
    the_text = get_text()

    # 3) Calls get_key_character() and stores the return value in the variable key_character.
    key_character = get_key_character()
    
    # 4) Calls first_ten_words(the_string) with the parameter the_text and stores the return value in the variable text_summary.
    text_summary = get_first_ten_words(the_text)
    print("\nThe first ten words of the blog_entry as a summary of the entry:", text_summary )

    # 5) Calls mask_character(the_string, key_character) with the parameters the_text and key_character and stores the return value in the variable new_string.
    new_string = mask_character(the_text, key_character)
    print("\nString with key character,", key_character, "masked:", new_string)

    # 6) Calls count_key() and stores the return value in the variable num_keys.
    num_keys = count_key(the_text, key_character)
    print("\n# of occurences of key character,", key_character, ":", num_keys)

# Call main function.
main()

''' 
---------------------------------------Sample Run---------------------------------------
Enter user name: H

Error: user name must be at least 2 characters.
Enter user name: Hanan

Enter text: sdff

Error: text must be at least 100 characters.

Enter text: Whether computer science is one of your college courses or just something of casual interest.

Error: text must be at least 100 characters.

Enter text: Whether computer science is one of your college courses or just something of casual interest, this blog post is dedicated to you. Detailing 30 of the best computer science blogs, this list is a place to start; continue your own education and find enriching, intriguing topics related to this rapidly changing discipline, no matter your level of experience or your background.

Enter key character: c

The first ten words of the blog_entry as a summary of the entry: Whether computer science is one of your college courses or

String with key character, c masked: Whether *omputer s*ien*e is one of your *ollege *ourses or just something of *asual interest, this blog post is dedi*ated to you. Detailing 30 of the best *omputer s*ien*e blogs, this list is a pla*e to start; *ontinue your own edu*ation and find enri*hing, intriguing topi*s related to this rapidly *hanging dis*ipline, no matter your level of experien*e or your ba*kground.

# of occurences of key character, c : 19
---------------------------------------End Sample Run---------------------------------------
'''