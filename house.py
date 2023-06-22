# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:51:48 2023

@author: James Fehr
"""
name = input(" What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print(" Gryffindor\n")
    case "Draco":
        print(" Slytherin")
    case _:
        print(" Who? \n")
    

