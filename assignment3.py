# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:22:40 2017

@author: Samir
"""

a = "Hello, World!"

grades = [80,90,100,70]
average = sum(grades)/len(grades)

grades_more = [50,20,60,100]

allgrades = grades + grades_more

grades[]
g=0
while g != -1:
    g = int(input("Enter Grade: "))
    print("User entered " + str(g))
    if not g == -1:
        grades.append(g)

if len(grades) > 0:
    

    average = sum(grades)/len(grades)
    
    if average >= 90:
        print("Grade is A")
    elif average >= 80:
        print("Grade is B")
    elif average >= 70:
        print("Grade is C")
    else:
        print("Grade is F")
        
else:
    print("did you forget to enter grades?")
    
    