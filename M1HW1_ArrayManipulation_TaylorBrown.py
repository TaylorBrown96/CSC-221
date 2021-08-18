# A brief description of the project
# Date: 17AUG21
# CSC221 M1HW1 – Array Manipulations
# Taylor J. Brown

# Prompt the user with a menu that has five options. 
# 1) Create a 3-by-3 Array
# 2) Display cube Values for elements in array
# 3) Add 7 to every element and display result
# 4) Multiply elements by 6 and display result
# 5) Exit
# --- Option 1 must be done first. If another option is selected give user an error message and display menu again ---
# Option 1. User is prompted to enter nine integers. Display a 3x3 array without brackets.
# Option 2. Will display the cube of each element in array. (Don’t modify the array. Copy then modify).
# Option 3. Add 7 to each element in array and display. (Don’t modify the array. Copy then modify).
# Option 4. Multiply each element in array by 6 and display. (Don’t modify the array. Copy then modify).
# Option 5. Terminate program.
# If any option other than 1-5 is entered give the user an error message and display menu again.
# After every operation, menu will be displayed again until user chooses to terminate the program.

import numpy as np
import copy

def main():
    array = ([])
    keep_going = 0
    while keep_going == 0:
        print('MENU')
        print('-'*25,'\n')
        print(''*3,'1) Create a 3-by-3 Array')
        print(''*3,'2) Display cube Values for elements in array')
        print(''*3,'3) Add 7 to every element and display result')
        print(''*3,'4) Multiply elements by 6 and display result')
        print(''*3,'5) Exit')
        usr_inp = int(input("Menu selection: "))
        
        if usr_inp == 1:
            array = option_1()
        elif usr_inp == 2:
            option_2(array)
        elif usr_inp == 3:
            option_3(array)
        elif usr_inp == 4:
            option_4(array)
        elif usr_inp == 5:
            keep_going +=1
        else:
            print("Error invalid option!")  
    
def option_1():
    L1 = []
    L2 = []
    L3 = []
    count1 = 9
    count = 0
    
    for count1 in range(count1):
        count += 1
        usr_inp = int(input(f'Please enter integer {count} of 9: '))
        z = len(L1)
        k = len(L2)
        if z < 3:
            L1.append(usr_inp)
        elif z == 3 and k < 3:
            L2.append(usr_inp)
        else:
            L3.append(usr_inp)

    array = np.array((L1,L2,L3), dtype = int)
    new_arr = array.reshape(3,3)
    printer(new_arr)
    
    return new_arr

def option_2(array):
    z = len(array)
    cpy_arr = copy.deepcopy(array)
    
    if z >= 1:
        sq_arr = cpy_arr ** 3
        printer(sq_arr)
        
    else:
        print("The array is empty! You have to create an array first!")

def option_3(array):
    z = len(array)
    cpy2_arr = copy.deepcopy(array)
    
    if z >= 1:
        add_arr = cpy2_arr + 7
        printer(add_arr)
        
    else:
        print("The array is empty! You have to create an array first!")
    
def option_4(array):
    z = len(array)
    cpy3_arr = copy.deepcopy(array)
    
    if z >= 1:
        multi_arr = cpy3_arr * 6
        printer(multi_arr)

    else:
        print("The array is empty! You have to create an array first!")

def printer(array):
    print()
    for row in array:
        for col in row:
            print(col, end=" ")
        print()  
    
    print()    

main()