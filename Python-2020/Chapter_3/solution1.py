
winning_number = 10

num = int(input("Enter you number:  "))

if num == winning_number:
    print ("YOU WIN")
else:
    if num < winning_number :
        print (" You enter number is Too Low")
    else:
        print ("You enter number is Too High")
