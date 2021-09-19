
num = list(range(1,11))

numbers = []
for i in num:
    if i % 2 == 0:
        numbers.append(i*2)
    else:
        numbers.append(-i)

print(numbers)


number = [ i *2 if i % 2 == 0  else -i for i in num ]
print (number)