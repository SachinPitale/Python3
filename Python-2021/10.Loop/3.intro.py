"""
Loops:
All programming language need a way to execute block of code many times, this is possible with loops.

Python has two types of loops:
for loop
while loop


for loop:
This loop in python is used to iterate over a sequence(list,tuple,string) or other iterable object

While loop:
while loop is used to execute a block of statement repeatedly until a  given a condition is satisfied
"""

my_list =  [3,4,34,5,67,89,23]

for i in my_list:
    print (i)
    rem=i%2
    if rem==0:
        print (f"{i} is even")
    else:
        print (f"{i} is old")
