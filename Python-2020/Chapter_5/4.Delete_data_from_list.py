# pop method : This method bydefault removed last element in last 
#               We can pass position number in pop so that we can  remove the element
# del method : we can remove data from list using position number
# remove method : some time we don't know the position that time we can use remove method


fruit = ["apple","mango","orange","grapes","watermelon"]

print (fruit)

# pop method : This method bydefault removed last element in last

fruit.pop()
print (fruit)
#  We can pass position number in pop so that we can  remove the element

fruit.pop(2)
print (fruit)

# del method : we can remove data from list using position number

number = [1,2,3,4]
del number[2]
print (number)
# remove method : some time we don't know the position that time we can use remove method

number.remove(1)
print (number)



