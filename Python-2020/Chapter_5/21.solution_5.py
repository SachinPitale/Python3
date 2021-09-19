

list1 = [1,2,3,4]
list2 = [1,2,8,9]


def common(list1,list2):
    list3 = []
    for i in list1:
        for e in list2:
            if i == e:
                list3.append(i)
    return list3


print (common(list1,list2))

       
