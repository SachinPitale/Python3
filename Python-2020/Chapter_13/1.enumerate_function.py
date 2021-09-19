# we use enumerate function with for loop to track postion of our 
#  item in iterable

# How we can do this without enumerate functions


names = ['abc','xty', 'pqr']
pos = 0

for i in names:
    print (f"{pos} -------> {i}")
    pos += 1


for pos, i in enumerate(names):
    print (f"{pos} -------> {i}")

# Define a function that take two arguments
#  1. list containing string
#  2. string that want to find in you list
#  and this function will return the index of string in your list and if string is not present then return -1


def find_pos (l,target):
    for pos, i in enumerate(l):
        if i == target:
            return pos
        return -1

print (find_pos(names,'pqr'))


