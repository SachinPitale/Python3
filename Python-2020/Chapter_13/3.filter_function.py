
def is_even(a):
    return a % 2 == 0

num = [1,2,6,3,4,5,7,8,9,10,11,12,13,14]
even = tuple (filter(is_even, num))
print (even)


even_num = filter(lambda a: a %2 == 0, num )

for i in even_num:
    print (i)


even_num = [i for i in num if i % 2 ==0]

print (even_num)