import os.path


class Person:
    def __init__(self, firstName, lastName, email):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def print_stuff(self):
        print(self.__firstName, self.__lastName, self.__email)

    def set_email(self, email):
        self.__email = email
    
    def get_firstName(self):
        return self.__firstName
        
    def get_lastName(self):
        return self.__lastName
    
    def get_email(self):
        return self.__email


class Employee(Person):
    def __init__(self, firstname, lastname, email, position, salary, full_part_time):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.position = position
        self.salary = salary
        self.full_part_time = full_part_time
        
        
    def write_to_file(self):
        file_exists = os.path.exists('Employees.txt')
        
        if file_exists == True:
            with open('Employees.txt', 'a') as f:
                f.write('\n' + f'{self.firstname:<13}{self.lastname:<12}{self.email:<26}{self.position:<11}{self.full_part_time:<12}{self.salary:<10}')

        else:
            with open('Employees.txt', 'w+') as f:
                f.write(f'{"First Name" :<13}{"Last Name" :<12}{"Email(company email)" :<26}{"Position" :<11}{"Full/Part" :<12}{"Salary" :<10}' + '\n')
                f.write(f'{self.firstname:<13}{self.lastname:<12}{self.email:<26}{self.position:<11}{self.full_part_time:<12}{self.salary:<10}')
    
            
            
def index(item):
    employee = Employee(item[0],item[1],item[2],item[3],item[4],item[5])
    employee.write_to_file()
    return

"""
# This is used to generate an Employees.txt file for testing.

x = Employee("Tom","Smith","smith.tom@company.com","Manager","2000","Full")                
x.write_to_file()
"""