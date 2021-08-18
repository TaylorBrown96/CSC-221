# Taylor J. Brown
# M1LAB1_Python_Review
# 18AUG21


def main():
    keep_going = 0
    nums = []
    
    while keep_going == 0:
        val = 0
        x = int(input("Please enter a number: "))
        z = x * 2 
        
        print("Your number doubled is:", z)
    
        nums.append(x)
        nums.append(z) 
        keep_going = vali(val)
        
    itera = len(nums)
    itera = int(itera / 2)
    index_1 = 0
    index_2 = 1
    for count in range(itera):
        print(f'Entered number {nums[index_1]}. Same number doubled {nums[index_2]}.')
        index_1 += 2
        index_2 += 2
    
def vali(val):
    """Menu for entering more numbers or exiting"""
    while val == 0:
        print("1. Enter another number.")
        print("2. Exit")
        usr_inp = int(input("Enter choice: "))
        
        if usr_inp == 1:
            val += 1
            return(0)
        elif usr_inp == 2:
            val += 1
            return(1)
        else:
            print("Please enter a valid number!")
    

if __name__ == "__main__":
    main()