user_info = {

      'name' : "sachin",
    'age' : 24,
    'mov' : ['AAA','BBB'],
    'MOU' : ['pqr','xyz']
}


print (user_info)
# Add the value in dict

user_info['SONGS'] = ['song1','song2']
print (user_info)

# remove the value in dict
# Pop method

user_info.pop('MOU')
print (user_info)
print (type(user_info))