# -*- coding: utf-8 -*-
"""Created on Wed Jun 21 13:17:10 2023

@author: James Fehr
# Implementation of a dictionary designed in the script
"""

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Ginny", "house": "Huffelpuff", "patronus": "Owl"}
    ]


for student in students:
    print(student["name"], student["house"],student["patronus"], sep=", ")
    
    