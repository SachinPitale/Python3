
def total (*args):
    print (args)
    mul = 1
    for i in args:
        mul *= i
    return mul

num = [2,3,9]
print (total(*num))