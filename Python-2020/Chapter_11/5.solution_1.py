

def number_qube (num,*args):
    qube = []
    for i in args:
        qube.append( i ** num )
    return qube

mylist = [i for i in range(11)]


print (number_qube(3, *mylist))



def qube (number,*args):
    if args:
        return [number ** i  for i in range(11) ]
    else:
        return "You did not pass any argument"


mylist = [i for i in range(11)]
print (number_qube(4, *mylist))
