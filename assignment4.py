# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:06:23 2017

@author: Samir
"""

installment = 1

no_of_months = int(input("Enter the no. of months: "))



for month in range(1,no_of_months + 1):
   
    if not month == 1:
        if month % 2 == 0:
            installment *= 2
        else:
            installment *= 3
    print("Month %s : $%s" %(str(month), str(installment)))
  