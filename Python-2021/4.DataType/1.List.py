# List is mutable
# Tuple is not mutable
"""
My_list=[]
My_list1=[4,5,6,7,'python']

print (My_list1, type(My_list1))
print (My_list1[0])
print (My_list1[-1][1])
print (My_list1[0:3])

My_list1[0]=3
print (My_list1)
"""

#To get index value of list
"""
my_list=[4,5,6,7,6,8]
my_list1=[11,12,13]
my_list2=[21,22,23]
print (my_list.index(5))
print (my_list.count(6)) # To count number of list value
my_new_list=my_list.copy() #Assign one list to other list
print (my_new_list)
my_list=my_list1.copy()
print (my_list)
my_list.append(9) # add value end of the list
print (my_list)

my_list.insert(5,98) # This will add new value based on index specifi
print (my_list)
print (dir(my_list))

my_list.reverse() # list the list in reverse order
print (my_list)

my_list.sort() # sorting list accending order
print (my_list)

my_list.pop() #remove last element of list
print (my_list)

my_list1.extend(my_list2) #merge one list to other list
print (my_list1)

"""

my_list=[4,5,6,7,6,8,22]
my_list1=[11,12,13,3,5]

my_list.remove(5)
print(my_list)

my_list.pop(3) # delete the index element
print(my_list)

my_list.extend(my_list1)
print (my_list)
my_list.sort()
print(my_list)
print(my_list[-1])