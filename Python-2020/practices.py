a , b , c = input("Enter your three numbers :   ").split(" ")
def greater(n1,n2,n3):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return "All number is same"



print (greater(a,b,c))

