

my_string="Working with for loop"
print (my_string)
for each_char in my_string:
    print (each_char)

print (" ".join(my_string))
print ("\n ".join(my_string))


my_list = [4,5,6,7,8]
for i in my_list:
    print (i)

my_list1 = [(1,2),(3,4),(5,6)]
for i in my_list1:
    print (i)

for i in my_list1:
    for m in 0, 1:
        print (i[m])


for i, j in my_list1:
    print (i)
    print (j)


my_dict = {"name": "sachin", "Profession": "IT", "Language": "Python"}

for i in my_dict.keys():
    print (i)
    
for i in my_dict.values():
    print (i)

for i in my_dict.items():
    print (i)

