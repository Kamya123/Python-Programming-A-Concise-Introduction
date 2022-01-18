# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:21:06 2021

@author: kamya
"""

#%%      
def problem2_1():
    lis = list(range(20,30))
    print(lis[3])
    print(lis)
    
    for i in lis:
        print(i, end = " ")
        
#%%  

alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"] 

def problem2_2(my_list):
    print(my_list)
    print(my_list[0])
    print(my_list[-1])
    print(my_list[3:5])
    print(my_list[0:3])
    print(my_list[3:])
    print(len(my_list))
    my_list.append("z")
    print(my_list)

#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for i in range(0, len(ne)):
        print(ne[i], "has", len(ne[i]), "letters.")
        
import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    for i in range(10) :
        print(random.randint(1,6))


def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    pass # replace this pass (a do-nothing) statement with your code

#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    print(random.randint(1,6) + random.randint(1,6))
    
#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter the length of side one:"))
    b = float(input("Enter the length of side two:"))
    c = float(input("Enter the length of side three:"))
    s =((.5)*(a+b+c))
    area =((s*(s-a)*(s-b)*(s-c))**.5)
    print("Area of a triangle with sides",a,b,c,"is",area)
    
#%%
def problem2_8(temp_list):
    sum = 0
    for i in range(0,len(temp_list)) :
        sum = sum + temp_list[i]
    average = sum/len(temp_list)
    print("Average:",average)
    print("High:",max(temp_list))
    print("Low:",min(temp_list))