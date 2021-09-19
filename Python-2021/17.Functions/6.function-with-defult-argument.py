"""
def display(num=1):
    print ("your default value is: ", num)
    return None

display(5)
display(7)
display() # If we pass no argument that time, it will use num=1 value as argument
"""

def add(a=0,b=0):
    result=a+b
    print(f"addition of {a} and {b} is : {result}")
    return None

add(5,7)
add()
add(18)