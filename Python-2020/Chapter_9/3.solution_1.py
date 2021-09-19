
name = ['abc','xyz','pqr']


rev = []
for i in name:
    rev.append(i[::-1])
print (rev)


name_1 = [i[::-1] for i in name]
print (name_1)