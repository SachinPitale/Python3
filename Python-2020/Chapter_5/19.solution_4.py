

#def odd_function(list):
#    odd_list = []
#    odd_list.append(list[::2])
#    return odd_list

#def even_function(list):
#    even_list = []
##    even_list.append(list[1::2])
#    return even_list







#number = [1,2,3,4,5,6,7,8,9,10,11]
##list_1 = odd_function(number)
# list_2 = even_function(number)

# numbers = []

# numbers.append(list_1)
# numbers.append(list_2)

# print (numbers)


def odd_even(list):
    even_list = []
    odd_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
    else:
            odd_list.append(i)
    output = [odd_list, even_list]
    return output

number = [1,2,3,4,5,6,7,8,9,10,11]
print (odd_even(number))