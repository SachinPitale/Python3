
# Show ticket pricing

# 1 to 3 = free
# 4 to 10 = 150
# 11 to 60 = 250
# 60 to above = 200


age = int(input("Enter you age :  "))

if age <= 3:
    print (" You can watch movie free")
elif age >= 4 and age <= 10:
    print ("You will have to pay 150 ruppes")
elif age <= 60 and age >= 11:
    print ("You will have to pay 250 rupees")
else:
    print ("you will have to pay 200 rupees") 


  