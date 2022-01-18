# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:41:09 2021

@author: kamya
"""

#%%
def problem1_1():
    print ("Problem Set 1")
    
#%%
def problem1_2(x,y):
    print (x+y)
    print (x*y)

#%%
def problem1_3(n):
    my_sum = 0
    for number in range(n+1):
        my_sum = my_sum + number
    print (my_sum)
    
#%%
def problem1_4(miles):
    feet = 5280*miles
    print("There are", feet, "feet in", miles, "miles.")
    
#%%
def problem1_5(age):
    if age < 7:
        print ("Have a glass of milk.")
    elif age < 21:
        print ("Have a coke.")
    else:
        print ("Have a martini.")
        
#%%
def problem1_6():
    for oddNumber in range(1, 100, 2):
        print(oddNumber, end=" ")
        
#%%
def problem1_7():
    b1 = float(input("Enter the length of one of the bases: "))
    b2 = float(input("Enter the length of the other base: "))
    h = float(input("Enter the height: "))
    A = (1/2)*(b1+b2)*h
    print("The area of a trapezoid with bases",b1,"and",b2,"and height",h, "is", A)