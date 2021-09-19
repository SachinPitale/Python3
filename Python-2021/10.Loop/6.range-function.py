
"""
range function:
##############
- It is build in function of python
- Generate the interger as list
syntax:
range(start,stop,step)
"""

print (range(1,10))
print (list(range(10)))
print (list(range(0,20,1)))
print (list(range(0,20,2)))
print (list(range(0,20,5)))
print (list(range(0,20,20)))
print (list(range(1,50,2)))

my_list = [6,7,8,9,"python"]
print (my_list)

print (len(my_list))
print (range(len(my_list)))
print (list(range(len(my_list))))


for each_index in range(len(my_list)):
    print (f'Index ---> {each_index} value of list ---> {my_list[each_index]}')

for i in range(10):
    print (i)