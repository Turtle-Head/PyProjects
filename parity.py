# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:19:31 2023

@author: James Fehr
"""

def isEven(n):
    #return True if n % 2 == 0 else False
    return n % 2 == 0

def main():
    x = int(input("What is x? "))
    if isEven(x):
       print("Even")
    else:
       print("Odd")
       
      
main()

    
    



