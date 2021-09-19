fruits = ["greps","mango","apple"] # list

fruits.sort()

print (fruits)

# We can't sort the tuple because it's immutable object
# but we can sort the tuple with help of sorted function 
# If we use sorted function it will give us list value
fruits1 = ("greps","mongo","apple") # tuple
print (sorted(fruits1))


# we can use sorted function with set 

fruits2 = {"greps","mango","apple"} #dict

print (sorted(fruits2))

guitars = [ 
    {'model': 'yamaha f310', 'price':8400},
    {'model': 'faith napture', 'price': 45000},
    {'model': 'honda h1', 'price': 130000},
    {'model': 'mercedics m1','price':220000}

]


print (sorted(guitars, key = lambda d:d['price']))
print (sorted(guitars, key = lambda d: d['price'], reverse = True))
