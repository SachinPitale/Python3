"""
def display(num):
    print(num)
    return None

display(4)
display() # When argument of variable we don't know
"""

def display(*kwarg): # when we want to pass multiple argument that time we usually used *kwarg
    print(kwarg)
    for each in kwarg:
        print (each)
        print (type(each))

display(4,5)
display(4)
display()

