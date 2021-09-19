#any or all function
#any : If it's get any occurance result will be True
#all : If it's get all the occurance result will be True otherwise False

numbers1 = [2,4,6,8,10]
even  = []
for i in numbers1:
    even.append(i % 2 == 0)


print (even)

even1 = (all([num % 2 == 0 for num in numbers1 ]) )
print (even1)

numbers2 = [2,4,6,9,10]

odd = (any([num % 2 == 0 for num in numbers2]))
print (odd)