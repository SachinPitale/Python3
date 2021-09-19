"""
def get_add(a,b):
    result=a+b
    #print(result)
    #return None # when use reture None it pass none value to other function.
    return result # if you want to pass variable value to other function must use return and variable name (ex: return variable)


def main():
    a=eval(input("Enter your first number : "))
    b=eval(input("Enter your first number : "))
    total=get_add(a,b)
    print(f"The addition of {a} and {b} is : {total}")
    return None

main()

"""
def multiply_by_10(value):
    return value * 10

def main():
    num=eval(input("Enter your number: "))
    result=multiply_by_10(num)
    print (f"{num} value is after multiply by 10: {result}")


main()