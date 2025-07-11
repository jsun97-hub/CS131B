'''
Program:  admit.py. 
Programmer: Jeffrey Sun
Date: 06/09/2025
Description:  The program compares two college applicants. The program should prompt for each student’s GPA, SAT, 
and ACT exam scores and report which candidate is more qualified on the basis of these scores.
'''

# Display intro message.
print("This program compares two applicants to determine which one seems like the stronger " \
"applicant. For each candidate I will need either SAT or ACT scores as well as a weighted GPA.")

# Prompt user for information about the first applicant.
exam_type = int(input("Information for the first applicant:\n\t do you have 1) SAT scores or 2) ACT scores? "))

# Conditional branching depending on exam_type.
if exam_type == 1:
    # Prompt user for more SAT information.
    s_math_score = int(input("SAT math? "))
    verbal_score = int(input("SAT verbal? "))
    gpa = float(input("overall GPA? "))
    max_gpa = float(input("max GPA? "))

    # Calculate score.
    sat_score = (2 * verbal_score + s_math_score) / 24.0
    gpa_score = gpa / max_gpa * 100.0

    # Compute score for the first applicant.
    applicant_1_score = sat_score + gpa_score

elif exam_type == 2:
    # Prompt user for more ACT information.
    english_score = int(input("ACT English? "))
    a_math_score = int(input("ACT math? "))
    reading_score = int(input("ACT reading? "))
    science_score = int(input("ACT science? "))
    gpa = float(input("overall GPA? "))
    max_gpa = float(input("max GPA? "))

    # Calculate score.
    act_score = (2 * reading_score + english_score + a_math_score + science_score) / 1.8
    gpa_score = gpa / max_gpa * 100.0

    # Compute score for the first applicant.
    applicant_1_score = act_score + gpa_score

# Prompt user for information about the second applicant.
exam_type = int(input("Information for the second applicant:\n\t do you have 1) SAT scores or 2) ACT scores? "))

# Conditional branching depending on exam_type.
if exam_type == 1:
    # Prompt user for more SAT information.
    s_math_score = int(input("SAT math? "))
    verbal_score = int(input("SAT verbal? "))
    gpa = float(input("overall GPA? "))
    max_gpa = float(input("max GPA? "))

    # Calculate score.
    sat_score = (2 * verbal_score + s_math_score) / 24.0
    gpa_score = gpa / max_gpa * 100.0

    # Compute score for the second applicant.
    applicant_2_score = sat_score + gpa_score

elif exam_type == 2:
    # Prompt user for more ACT information.
    english_score = int(input("ACT English? "))
    a_math_score = int(input("ACT math? "))
    reading_score = int(input("ACT reading? "))
    science_score = int(input("ACT science? "))
    gpa = float(input("overall GPA? "))
    max_gpa = float(input("max GPA? "))

    # Calculate score.
    act_score = (2 * reading_score + english_score + a_math_score + science_score) / 1.8
    gpa_score = gpa / max_gpa * 100.0

    # Compute score for the second applicant.
    applicant_2_score = act_score + gpa_score

# Print overall scores.
print("\nFirst applicant overall score =", f'{applicant_1_score:.2f}')
print("Second applicant overall score =", f'{applicant_2_score:.2f}')

# Display final report.
if applicant_1_score == applicant_2_score:
    print("The two applicants seem to be equal.")
elif applicant_1_score > applicant_2_score:
    print("The first applicant seems to be better.")
else:
    print("The second applicant seems to be better.")

'''
-------------------------- Sample Run 1 --------------------------
This program compares two applicants to determine which one seems like the stronger applicant. For each candidate I will need either SAT or ACT scores as well as a weighted GPA.
Information for the first applicant:
         do you have 1) SAT scores or 2) ACT scores? 1
SAT math? 450
SAT verbal? 530
overall GPA? 3.4
max GPA? 4.0
Information for the second applicant:
         do you have 1) SAT scores or 2) ACT scores? 2
ACT English? 25
ACT math? 20
ACT reading? 18
ACT science? 15
overall GPA? 3.3
max GPA? 4.0

First applicant overall score = 147.92
Second applicant overall score = 135.83
The first applicant seems to be better.
------------------------- End Sample Run 1 ------------------------

-------------------------- Sample Run 2 --------------------------
This program compares two applicants to determine which one seems like the stronger applicant. For each candidate I will need either SAT or ACT scores as well as a weighted GPA.
Information for the first applicant:
         do you have 1) SAT scores or 2) ACT scores? 2
ACT English? 20
ACT math? 19
ACT reading? 21
ACT science? 30
overall GPA? 3.5
max GPA? 4.0
Information for the second applicant:
         do you have 1) SAT scores or 2) ACT scores? 1
SAT math? 610
SAT verbal? 640
overall GPA? 4.3
max GPA? 5.0

First applicant overall score = 149.17
Second applicant overall score = 164.75
The second applicant seems to be better.
------------------------- End Sample Run 2 ------------------------

-------------------------- Sample Run 3 --------------------------
This program compares two applicants to determine which one seems like the stronger applicant. For each candidate I will need either SAT or ACT scores as well as a weighted GPA.
Information for the first applicant:
         do you have 1) SAT scores or 2) ACT scores? 1
SAT math? 510
SAT verbal? 530
overall GPA? 3.4
max GPA? 4.0
Information for the second applicant:
         do you have 1) SAT scores or 2) ACT scores? 1
SAT math? 570
SAT verbal? 500
overall GPA? 3.4
max GPA? 4.0

First applicant overall score = 150.42
Second applicant overall score = 150.42
The two applicants seem to be equal.
------------------------- End Sample Run 3 ------------------------
'''