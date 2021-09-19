# insert method : It's use to insert the date in any position
# append method : it's use to insert data in last of the list
# How to join to list
# extend method : it's method is used for join the two string

fruit1 = ["grapes","orange"]

print (fruit1)

fruit2 = ["apple","mango"]
print (fruit2)
# insert method

fruit1.insert(1, "watermelon")

print (fruit1)

# Join method

fruit = fruit1 + fruit2
print (fruit)

# extend method 

fruit1.extend(fruit2)
print (fruit1)
print (fruit2)

