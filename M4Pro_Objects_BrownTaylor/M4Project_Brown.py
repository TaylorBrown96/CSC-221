# Taylor J. Brown
# M4Project_Brown.py
# 21NOV21


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