numbers = [1,2,3,4]


def square (a):
    return i**2



print (map(square, numbers))

square = list(map(lambda a: a**2, numbers ))
print (square)

# list comprehension
squares_new =  [i**2 for i in numbers]
print (squares_new)


names = ['abc','abcd','abcde']
length = map(len, names)

new_list = list (map(len, names))
print (new_list)
print (length)

for i in length:
    print (i)

    