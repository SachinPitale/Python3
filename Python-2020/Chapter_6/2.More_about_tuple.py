# looping in tuples
# tuple with one element
# tuple without parathesis
# tuple unpacking 
# list inside tuple 
# some functions that you can use with tuples


mixed = (1,2,3,4,5)

for i in mixed:
    print (i)



print ("This is while loop")
i =1
while i <= len(mixed):
    print (i)
    i = i + 1


# tuple with one element , We neccessary to , after the element
number = (1,)    
print(type(number))

# tuple without parathesis

words = 'word1','word2','word3'
print (type(words))
print (words)

# tuple unpacking 

names = ("Rajesh","Suresh","Yogesh")
name1,name2,name3, = (names)
print (name1)

# list inside tuple 

fruits = ("mango","apple",["banana","kiwk","orange"])

fruits[2].append("watermelon")
print (fruits)




# some functions that you can use with tuples


mixed = (1,2,3,4,5)

print (min(mixed))

print (max(mixed))




print (sum(mixed))