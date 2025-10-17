'''
Expected Output
Enter data for two persons.
Enter the first name: Alexis
Enter the last name: Martinez
Enter the job title: Web Application Programmer
Enter the first name: Harris
Enter the last name: LeBlanc
Enter the job title: Pen Tester
Alexis Martinez
Web Application Programmer
Harris LeBlanc
Pen Tester
'''

class Techie:
    def __init__(self, first_name, last_name, job_title):
        self.first = first_name
        self.last = last_name
        self.title = job_title
    # create a function to return the Person's first name
    def get_first(self):
        return self.first
    # create a function to return the Person's last name
    def get_last(self):
        return self.last
    # create a function to return the Person's profession
    def get_title(self):
        return self.title

def main():
    # Get information for two persons.
    print("Enter data for two persons.")

    # Get info for the first person.
    first1 = input("Enter the first name: ")
    last1 = input("Enter the last name: ")
    job1 = input("Enter the job title: ")


    # Get info for the second person.
    first2 = input("Enter the first name: ")
    last2 = input("Enter the last name: ")
    job2 = input("Enter the job title: ")

    # Instantiate Techie class with information for the two persons.
    techie1 = Techie(first1, last1, job1)
    techie2 = Techie(first2, last2, job2)

    # Print names and jobs for techie1 and techie2
    print(techie1.get_first(), " " , techie1.get_last(), "\n", techie1.get_title(), sep = "")
    print(techie2.get_first(), " ", techie2.get_last(), "\n", techie2.get_title(), sep = "")

main()