
# Create list of square for 1 to 10 numbers


square = []

for i in range(1,11):
    square.append(i**2)
print (square)

square_1 = [i**2 for i in range(1,11)]
print (square_1)


# Create list for -1 to -10 numbers

num = []
for i in range(1,11):
    num.append(-i)
print (num)

num_1 = [-i for i in range(1,11)]
print (num_1)

# Print only frist later of each value

names = ['Yogesh','Suresh','Naresh']

name = []
for i in names:
    name.append(i[0])
print (name)


name_1  = [i[0] for i in names]
print (name_1)