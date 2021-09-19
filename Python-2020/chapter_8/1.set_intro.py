# set data type : unordered collection of unique order
# we can store in set is integer, floating point, string
# we can not store any dict and list in set
# we define set using {}

s = {1,2,3,2}
print (s)

# To remove the duplicate value for set
list1 = [1,2,3,4,5,6,7,6,7,8,9,9]
print(list1)

list1 = list(set(list1))
print(list1)

#  To add the value in set using add method

s1 = {1,2,3,}

s1.add(4)
print (s1)
# Remove the value from set using remove methond and discard method
s1.remove(2)
print (s1)

s1.discard(5) # If value is not exist in set it will not give any error
print (s1)

# Copy one set to other set

s2 = s1.copy()
print (s2)