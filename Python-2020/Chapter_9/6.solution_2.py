
my_list = ['True', 'False', [1,2,3],1, 1.0, 3]

num = []
for i in my_list:
    if type(i) == int or type(i) == float:
        num.append(i)
print (num)


numbers = [i for i in my_list if (type(i) == int or type(i) == float )]
print (numbers)