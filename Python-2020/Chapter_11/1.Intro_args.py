# *args we used in function to pass multipe value to execute
# We are calculating the number 


def total (*args):
    total = 0
    for num in args:
        total += num 
    return total

print (total(1,2,3,4,5,6,7,8,9,10,11,12))