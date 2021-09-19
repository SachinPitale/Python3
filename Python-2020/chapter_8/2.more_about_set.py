s = {1,2,3,4}

# If loop

if 1 in s:
    print ("number is present")
else:
    print ("number is absent")

# for loop

for i in s:
    print(i)

# Union and intersection

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print ("Union value is", s1 | s2)
print ("intersection value is", s1 & s2)
