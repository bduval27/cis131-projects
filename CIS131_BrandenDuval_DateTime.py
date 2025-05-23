'''
script: Assignment: Manipulating Dates and Times with Module: DATETIME
action: 
        a) gets the current date time and stores it as x
        b) repeats part (a) and stores the result as y
        c) displays each datetime object
        d) displays each datetime object's data attributes individually
        e) uses comparison operators to compare the two datetime objects
        f) calculates the difference between y and x
author: Branden Duval
date:   03/10/2025
'''

# importing the necessary module
import datetime as dt

# Part A: Get the current date and time and store it in variable x
x = dt.datetime.now()

# Part B: Repeat Part(a) and store it in variable y
y = dt.datetime.now() 

# Part C: Display each datetime object
print('Date 1:',x)
print('Date 2:',y,'\n') # added new line to make the output more legible in the terminal

# Part D: Display each datetime obect's data attributes individually
print('Date 1 Month:', x.month)
print('Date 1 Day:', x.day)
print('Date 1 Year:', x.year)
print('Date 1 Hour:', x.hour)
print('Date 1 Minute:', x.minute)
print('Date 1 Second:', x.second)
print('Date 1 Microsecond:', x.microsecond,'\n') # new line added for legibility

print('Date 2 Month:', y.month)
print('Date 2 Day:', y.day)
print('Date 2 Year:', y.year)
print('Date 2 Hour:', y.hour)
print('Date 2 Minute:', y.minute)
print('Date 2 Second:', y.second)
print('Date 2 Microsecond:', y.microsecond,'\n') # new line added for legibility

# Part E: Use the comparison operators to compare the two datetime objects
comp1 = x > y
print('Date 1 > Date 2?', '\n',comp1)
comp2 = x < y
print('Date 1 < Date 2?', '\n',comp2)
comp3 = x <= y
print('Date 1 <= Date 2?', '\n',comp3)
comp4 = x >= y
print('Date 1 >= Date 2?', '\n',comp4)
comp5 = x != y
print('Date 1 != Date 2?', '\n',comp5)
comp6 = x == y
print('Date 1 = Date 2?', '\n',comp6,'\n') # added new line for legibility

# Part F: Calculate the difference between y and x
yMinusx = y - x
print('Date 2 - Date 1 =',yMinusx)