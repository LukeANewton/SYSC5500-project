# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:41:47 2020

@author: luken

This short script aids in the build process for our UPPAAL model.

The script will print to the console a number of automata instatiations 
that follow UPPAAL's syntax. This console output can be copied into the UPPAAL
system declaration to help create larger models. You can specify the number of
devices insatntiated, as well as the number of possible device passwords.
Passwords are selected unifomly randomly.

This is helpful for larger models becuase unfortunately, UPPAAL does not 
support use of looping or arrays in their system declarations, so you need a 
separate line to instantiate each device in the model.

to run this file, you need python 3.7, and simply type "python system_declaration_helper.py"
"""
import random

NUMBER_DEVICES = 100
NUMBER_CREDENTIALS = 10

# print bot initialization with random selected credentials
for i in range(1, NUMBER_DEVICES+1):
    print("BOT",i," = Bot_t1(",i,",",random.randint(101, 100+NUMBER_CREDENTIALS),");",sep="")
 
# this is just a line break to help separate the console output
print();   
 
# print list of instantiated bots to append to system declaration
s = "BOT1,"
for i in range(2, NUMBER_DEVICES):
    s +=" BOT"+str(i)+","
s += " BOT"+str(NUMBER_DEVICES)+";"
print(s)