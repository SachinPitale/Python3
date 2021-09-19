num1 = eval(input("Enter your number: "))

if num1=="1":
    print (" you enter number one")
if num1=="2":
    print (" you enter number two")
if num1=="3":
    print (" you enter number three")
if num1=="4":
    print (" you enter number four")
if num1=="5":
    print (" you enter number five")

if num1 not in [1,2,3,4,5]:
    print ("You enter out of range value, enter valid number between 1-5 range")