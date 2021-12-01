# Taylor J. Brown
# M4Project_Brown.py
# 21NOV21


"""
    Present the user with 3 options 

    1) Enter Employee info
    2) Read Employee info
    3) Exit

    *If the user chooses option 1 send them to a gathering function*
    
    Ask the user how many employees they would like to enter and iterate through the
    next part x amount of times

    Ask for the employees first name

    Ask for the employees last name

    Create the employees email with the format "lastname.firstname@company.com"

    Ask for employees position with the company

    Ask if the employee if part time or full time

    Ask for the employees salary

    Append all inquires as a list to a nested list 

    Iterate through each object in the nested list and pass them through the Employee class 
    in the person.py

    Check if the Employees.txt file exist
        -If the file doesnt exist, create the file and write the column headers 
        -If the file does exits write each new employee onto the next line of the file 

    *If the user chooses option 2 open the Employee.txt and print each line of the file*

    *If the user chooses option 3 terminate the program*

    *If the user chooses anything other than the 3 given present with an error and ask for a new input*
"""


import person

def main():
    keep_going = True
    
    while keep_going == True:
        print("1) Enter Employee info")
        print("2) Read Employee info")
        print("3) Exit")
        usr_inp = input(">")
        if usr_inp == "1":
            Enter_Employee()
        elif usr_inp == "2":
            print_file()
        elif usr_inp == "3":
            keep_going = False
        else:
            print("please enter a valid option!")


def Enter_Employee():
    employees = []
    num_employees = int(input("How many employees would you like to enter?"))
    
    for _ in range(num_employees):
        first_name = input("\nWhat is the employees first name?: ")
        last_name = input("What is the employees last name?: ")
        email = last_name.lower() + "."+ first_name.lower()+ "@company.com"
        postion = input("What is this employees position with this company?: ")
        salary = input("What is this employees salary?: ")
        
        keep_going = True
        while keep_going == True:
            usr_inp = input("Is this employee full time?(y or n): ")
            
            if usr_inp.lower() == "y":
                full_part_time = "Full"
                break
            elif usr_inp.lower() == "n":
                full_part_time = "Part"
                break
            else:
                print("Please enter a valid option!") 
                
        employee = [first_name,last_name,email,postion,salary,full_part_time]
        employees += [employee]
        
    for element in employees:
        person.index(element)
        
        
def print_file():
    try:
        with open('Employees.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)
        print()
    except:
        print("There isn't an Employees.txt file in this folder!\n")
                
if __name__ == "__main__":                
    main()