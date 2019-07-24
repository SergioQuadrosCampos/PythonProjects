# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:45:46 2019

@author: sergioq

"""
"""
Objetive: Find PI to the Nth Digit
Description: Enter a number and have the program generate PI up to that many
decimal places. Keep a limit to how far the program will go.


Predict learning: 
    Learn Function. 
    Learn numbers types.
    Learn numbers manipulation.
    Laern to calculate PI.
    
How to solve:
    As we need to have Nth digit we will need one variable in the function. 
    find out how to calculate PI to the 2th number. 
    Create an algurithm to make the variable be Nth number.
    Test for bugs and put a limit. 


Problems:
    Math.pi just have like 10 decimals.
    Need to find a way to find out the other decimals.
    How do you calcule the PI as it is a constant? Save all the values? 
    
"""

import math

somepi = round(math.pi, 20)
print (len(str(math.pi)))

b='{:.49f}'
print('PI = ' + b.format(math.pi))
#def PI2Nth(Nthnumber):
    


"""
    What I learned:
        Most builtin modules are written in C.  
        You can't use the module inspect to read them or where the file is located.
        You can read the original code on https://github.com/python/cpython. But couldn't find how they defined PI there. 
        This problem is harder than I thought. 
        Wrapper function is a simple function that calls another functions or multiples function.
        jyuuic2 methord only go to 49th place. Probably used the saved method. 
        There a three math algorithm to find PI (Archimedes, Machin, Chudnovsky)
        PI is algorithm is O(n²)
"""