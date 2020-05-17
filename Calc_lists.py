# -*- coding: utf-8 -*-
"""
@author: DUDO3
"""

from Calc_class import Calculator

#Operator menu to select functions for simple calculator incl. description
def operator_menu():
    print('Operator no.'.ljust(16), 'Operation'.ljust(15),
          'Operator description'.ljust(25), sep='')
    print('1'.center(16), 'add'.ljust(15), 'to do addition'.ljust(25), sep='')
    print('2'.center(16), 'sub'.ljust(15),
          'to do subtraction'.ljust(25), sep='')
    print('3'.center(16), 'multiply'.ljust(15),
          'to do multiplication'.ljust(25), sep='')
    print('4'.center(16), 'divide'.ljust(15),
          'to do division of numbers'.ljust(25), sep='')
    print('5'.center(16), 'square_root'.ljust(15),
          'to square_root'.ljust(25), sep='')
    print('6'.center(16), 'square'.ljust(15),
          'to perform square'.ljust(25), sep='')
    print('7'.center(16), 'power'.ljust(15),
          'to perform power to number'.ljust(25), sep='')
    print('8'.center(16), 'SumL'.ljust(15),
          'to return summary of a single list'.ljust(25), sep='')
    print('9'.center(16), 'lbs=>kg'.ljust(15),
          'to convert pounds to kg'.ljust(25), sep='')
    print('10'.center(16), 'C=>F'.ljust(15),
          'to convert degree Celsius to Fahrenheit'.ljust(25), sep='')
    print('11'.center(16), 'odd'.ljust(15),
          'return odd numbers from list'.ljust(25), sep='')
    print('12'.center(16), 'even'.ljust(15),
          'return even numbers from list'.ljust(25), sep='')    
    print('13'.center(16), 'pyth_triplets'.ljust(15),
          'returns pythagorean triplets using ()'.ljust(25), sep='')   

#passing list of numbers into calculation process
def process_operation():
    operator_menu()
    func = input('Enter operator?')

    if func in ['13', 'pyth']:
        n = int(input("Enter n value: ")) 
        print(n)

    if func not in ['13', 'pyth_triplets']:
        x = list(map(float, input("Enter xlist of numbers (space separated): ").split())) 
        print(x)
    
    if func not in ['5', '6', '8', '9', '10', '11', '12', '13', 'sqrt', 'square',
                    'SumL', 'lbs=>kg', 'C=>F', 'odd', 'even', 'pyth_triplets']:
        y = list(map(float, input("Enter ylist of numbers (space separated): ").split())) 
        print(y)
        
    if func in ['1', '+']:
        print('Result:', Calculator().add(x,y))
    if func in ['2', '-']:
        print('Result:', Calculator().sub(x,y))
    if func in ['3', '*']:
        print('Result:', Calculator().multi(x,y))
    if func in ['4', '/']:
        print('Result:', Calculator().div(x,y))
    if func in ['5', 'sqrt']:
        print('Result:', Calculator().square_root(x))
    if func in ['6', 'square']:
        print('Result:', Calculator().square(x))
    if func in ['7', 'pwr()']:
        print('Result:', Calculator().power(x,y))
    if func in ['8', 'SumL']:
        print('Result:', Calculator().sumlist(x))
    if func in ['9', 'lbs=>kg']:
        print('Result:', Calculator().conv_lbs_to_kg(x), 'kg')
    if func in ['10', 'C=>F']:
        print('Result:', Calculator().conv_C_to_F(x), 'Farenheit')
    if func in ['11', 'odd']:
        print('Result:', Calculator().odd(x))
    if func in ['12', 'even']:
        print('Result:', Calculator().even(x))
    if func in ['13', 'pyth_triplets']:
        print(Calculator().pyth_triplets(n))

def calculator():
    go_again = ''
    while go_again != 'n':
        process_operation()
        go_again = input('Would you like to continue (y/n)?')

calculator()







