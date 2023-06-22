# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:49:55 2023

@author: James Fehr
"""
def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
           break
    return n

    
def meow(n):
    for _ in range(n):
        print("Meow")

def main():
    n = get_number()
    meow(n)
    

main()

