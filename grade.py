# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:22:23 2023

@author: James Fehr
"""
score = int(input(" Score: "))

if  90 <= score <= 100:
    print(" Grade: A\n")
elif  80 <= score < 90:
    print(" Grade: B")
elif 70 <= score < 80:
    print(" Grade C\n")
elif 60 <= score < 70:
    print(" Grade D\n")
elif  50 <= score < 60:
    print(" Grade F\n")
else:
    print(" Grade F \n Did you attend class?")
    