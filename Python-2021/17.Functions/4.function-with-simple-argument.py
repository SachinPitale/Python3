"""

def get_result(num): #Parameter and positional argument
    result=num+10
    print(f"final result of num is {result}")
    return None

def main():
    num=eval(input("Enter your number: "))
    get_result(num) #Argument
    return None



main()
"""


def get_add(p,q):
    result=p+q
    print(f"The addition of {p} and {q} is : {result}")
    return None  

def get_sub(m,n):
    result=m-n
    print(f"The sub of {m} and {n} is : {result}")
    return None

def main():
    a=eval(input("Enter your first number:  "))
    b=eval(input("Enter your second number:  "))
    get_add(a,b)
    get_sub(b,a)
    get_sub(109,16)
    x=50
    get_add(x,b)
    get_sub(b,x)
    return None


main()

