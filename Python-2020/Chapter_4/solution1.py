

def greater_number(a,b):
    if a > b:
        return "a is greater than b"
    return "b is greater than a"


num1 = int(input("Enter your 1st number : "))
num2 = int(input("Enter your 2nd number:  "))

value = greater_number(num1,num2)
print(value)