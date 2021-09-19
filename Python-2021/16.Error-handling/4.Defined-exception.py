"""
We can create custom exception using:
1. raise( Used to raise an existing exceptions)
2. assert(Used to create an AssertionError)
"""

'''
age=23


if age>30:
	print("Valid age")
else:
	raise ValueError("Age is less than 30")

'''

age=45

try:
	assert age>30
	print("Valid age")
except AssertionError:
	print("Raised with assert because age is lessthan 30")
except:
	print("Exception occured")
