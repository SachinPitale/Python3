


def total (num,*args):
    print (num)
    sum = 0
    for i in args:
        sum += i
    return sum

print (total(2,7,18))