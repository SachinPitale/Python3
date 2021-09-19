
# fromkeys : Assign multiple one value to multiple keys

user_info = dict.fromkeys (['name','movie','songs'], 'unknown' )

print (user_info)


# clear method : to remove key and values from dict
#user_info.clear()
# print (user_info)


# copy method : To copy one dict to other dict

d1 = user_info.copy()  
print (d1)