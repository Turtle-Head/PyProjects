# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:31:47 2023

@author: James Fehr
# Mario::broad strokes example of how to set up ascii designs via objects
"""

def main():
    print_square(3)
    
def print_column(height):
    for i in range(height):
        print("#\n" * height, end="")

def print_row(width):            
    print("#" * width)
        
def print_square(size):
    
    for i in range(size):
        print_row(size)
        
  
 
main()
