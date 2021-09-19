#number = [1 ,2, 3, 4]
#number.reverse()
#print(number)
#words = ["word1","word2","word3"]
#print (words[::-1])



#def reverse_list(list):
#    list.reverse()
#    return list

#def reverse_fun(list):
#    list[::-1]
#    return list 

#number = [1 ,2, 3, 4] 
#words = ["word1","word2","word3"]
#print (reverse_list(number))
#print (reverse_list(words))

#print (reverse_fun(number))
#print (reverse_fun(words))


def my_function(list):
    my_list = []
    for i in range(len(list)):
        num = list.pop()
        my_list.append(num)
    return my_list


number = [1 ,2, 3, 4] 
words = ["word1","word2","word3"]

print (my_function(number))
print (my_function(words))

