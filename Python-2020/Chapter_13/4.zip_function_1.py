users_id = ["user1","user2","user3"]
names = ["harshit", "mohit", "rohit"]

sqaures = (list(zip(users_id, names)))
print (sqaures)

sqaures1 = (dict(zip(users_id,names)))
print (sqaures1)

l1 = [1,3,5,7]
l2 = [2,4,6,8]

l = (list(zip(l1,l2)))
print (l)
l3,l4 = list(zip(*l))

print (l3)
print (l4)
my_list_even = []
my_list_odd = []
for pair in zip(l1,l2):
    my_list_even.append(max(pair))
    my_list_odd.append(min(pair))

print(my_list_even)
print(my_list_odd)


