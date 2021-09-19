def sub_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count


number = [1,2,3, [14,5],  [7,8]]

print (sub_list(number))



