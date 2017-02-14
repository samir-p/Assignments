# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 08:29:33 2017

@author: Samir
"""

base_premium = 50
age = int(input("Enter the age of the driver: "))

if age < 25:
    base_premium += 100
elif age < 35:
    base_premium += 20
    
no_of_accidents = int(input("Enter the number of accidents in the last 5 years of driver's history: "))


insurance_denied = False
surcharge_per_accident = 0


if no_of_accidents > 5:
    insurance_denied = True
elif no_of_accidents >= 3:
    surcharge_per_accident = 60
elif no_of_accidents == 2:
    surcharge_per_accident = 40

if not insurance_denied:
    total_premium = base_premium + surcharge_per_accident*no_of_accidents
    print("The total insurance for driver %s years old with %s accident(s) is $%s.00" % (age,str(no_of_accidents),str(total_premium)))
else:
    print("Based on your driver history, your insurance has been denied for this year.")
    
    
    
    
