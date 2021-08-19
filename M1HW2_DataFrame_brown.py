# A brief description of the project
# Date: 18AUG21
# CSC221 M1HW2 – DataFrame
# Taylor J. Brown

# Step A: Create a DataFrame named temperatures with columns named Maxine, James, and Amanda
# Step B: Create a DataFrame with the indices Morning, Afternoon, and Evening
# Step C: Display column Maxine
# Step D: Display row Morning
# Step E: Display rows Morning and Evening
# Step F: Display columns Amanda and Maxine
# Step G: Display elements for Amanda and Maxine in Morning and Afternoon
# Step H: Display descriptive statistics of temperatures
# Step I: Transpose
# Step J: Sort columns alphabetically

import pandas as pd

def main():
    temps = {'Maxine': [98,89,72], 'James': [90,92,103], 'Amanda': [89,81,100]}
    
    # Step A
    temperatures = pd.DataFrame(temps)
    print('Step A: Temperature DataFrame')
    print(temperatures, '\n')
    
    # Step B
    temperatures = pd.DataFrame(temps, index=['Morning','Afternoon','Evening'])
    print('Step B: Add indices')
    print(temperatures, '\n')
    
    # Step C
    print('Step C: Select column Maxine')
    print(temperatures[['Maxine']], '\n')
    
    # Step D
    print('Step D: Select row Morning')
    print(temperatures.loc[['Morning']], '\n')
    
    # Step E
    print('Step E: Select rows Morning and Evening')
    print(temperatures.loc[['Morning','Evening']], '\n')
    
    # Step F
    print('Step F: Select columns Amanda and Maxine')
    print(temperatures[['Maxine','Amanda']], '\n')
    
    # Step G
    print('Step G: Select elements for Amanda and Maxine from Morning and Afternoon')
    print(temperatures.loc['Morning':'Afternoon',['Amanda','Maxine']], '\n')
    
    # Step H
    print('Step H: Display descriptive statistics')
    print(temperatures.describe(), '\n')
    
    # Step I
    print('Step I: Transpose')
    print(temperatures.T, '\n')
    
    # Step J
    print('Step J: Sort column name alphabetically')
    print(temperatures.sort_index(axis=1, ascending = True))
    
main()
