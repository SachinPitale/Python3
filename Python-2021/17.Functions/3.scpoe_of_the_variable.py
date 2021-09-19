"""
We you want to access the  variable from one function to other function use the variable as a global or pass argument to the function.
if you want to access same variable multipe function then use  global.
If you want to access the same variable in only one function use the argument
"""

def myfunction1():
    x=60 # This is local variable
    print ("Welcome to python")
    print("x value of func1", x)
    return None

def myfunction2(y):  #Parameter
    print ("Thank you")
    print("y value of func2", y)  
    return None

def main():
    #global=x
    x=10
    myfunction1()
    myfunction2(x) #Argument

main()