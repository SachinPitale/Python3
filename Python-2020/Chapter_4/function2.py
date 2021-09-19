# print greater number between 3 numbers

def greater_number(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c

num1 = int(input("Enter your 1st number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter your Third number : "))




Bigger = greater_number(num1,num2,num3)
print (f"{Bigger} number is greater")