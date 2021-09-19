user_info = {

    'name' : "sachin",
    'age' : 24,
    'age' : 29,
    'mov' : ['AAA','BBB'],
    'MOU' : ['pqr','xyz']
}


# To check if key is exist in dictanry  

if 'name' in user_info:
    print ("present")
else:
    print ("Not present")


# To check if value is exist in dictanry

if 'sachin' in user_info.values():
    print ("present")
else:
    print("Not present")

# loop in dictionaries

for i in user_info:
    print (i)


print (" To print values ")
for i in user_info.values():
    print (i)

# values method
user_info_values = user_info.values()
print (user_info_values)

user_info_keys = user_info.keys()
print (user_info_keys)


#  Items method

for i  in user_info.items():
    print (i)

for i, j in user_info.items():
    if i == 'age':
        print (f" The key is {i} and value is {j}") 


   



