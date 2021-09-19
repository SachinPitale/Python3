my_dict = {'animal':'fox','fruit': 'apple', 1:'one','two':2}
print (my_dict)
print (my_dict['fruit'])
print (my_dict.get('animal'))
#print (my_dict['three'])
print (my_dict.get('three'))
print(my_dict)
#my_dict.clear()
#print (my_dict)
my_dict['three']=3
print (my_dict)
my_dict['animal']='dog'
print (my_dict)
print (my_dict.keys())
print (my_dict.values())
print (my_dict.items()) # it will get as one item
y=my_dict.copy() #it will assign my_dict dictionaries to y dictionaries
print(y)
print (id(my_dict), id(y))
new_dict={'number': 22}
my_dict.update(new_dict) # update method will merge one dictionaries to other dictionaries
print (my_dict)
my_dict.pop('number') #pop method will remove key value pair
print (my_dict)
my_dict.popitem()
print(my_dict)
my_dict.popitem()
print(my_dict)

keys=['a','b','c','d','e','f']
new_dict1=dict.fromkeys(keys)
print(new_dict1)
new_dict1['a']='First alpha'
print(new_dict1)
