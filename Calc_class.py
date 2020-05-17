# -*- coding: utf-8 -*-
"""
@author: DUDO3
"""
from functools import reduce

class Calculator():

    def __init__(self):
        self.x = []
        self.y = []

    def setx(self, x):
        self.x = x
        
    def sety(self, y):
        self.y = y  

    def add(self, x, y):
        return list(map(lambda x,y : x+y, x,y))

    def sub(self, x, y):
        return list(map(lambda x,y : x-y, x,y))
    
    def multi(self, x, y):
        return list(map(lambda x,y : x*y, x,y))

    def div(self, x, y):
        if 0 in y:
            print('Division by zero')
            return 'N/A'
        else:
            return list(map(lambda x,y : round(x/y, 2), x,y))
    
    def square_root(self, x):
        return list(map(lambda x : round(x**0.5, 2), x))

# square all numbers of list using map and lambda
    def square(self, x):
        return list(map(lambda x : x*x, x))
 
# power function taking list of numbers and list of the power numbers
    def power(self, x, y):
        return list(map(lambda x,y : x**y, x,y))

# using reduce to sum a list of numbers
    def sumlist(self, x):
        return reduce(lambda x,y: x+y, x)

# converting lbs to kg using lambda and map functions
    def conv_lbs_to_kg(self, x):
        return list(map(lambda x : round(x/2.20462262, 2), x))

# converting temperature from celsius to Farenheit using lambda and map functions
    def conv_C_to_F(self, x):
        return list(map(lambda x : round((x*(9/5)+32), 2), x))

# using lambda and filter functions for odd function to return odd numbers from list 
    def odd(self, x):
        return list(filter(lambda x : x % 2, x))

# using lambda and filter functions for odd function to return even numbers from list
    def even(self, x):
        return list(filter(lambda x : x % 2 == 0, x))

# using genarator function to return all pythagorean triplets in range of numbs
    def pyth_triplets(self, n):
        triplet_comp = ((x,y,z) for x in range(1,n) for y in range(x,n)
        for z in range(y,n) if x**2 + y**2 == z**2)
        for triplet in triplet_comp:
            print(triplet)





