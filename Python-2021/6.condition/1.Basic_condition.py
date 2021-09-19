

"""
If is called simple condition statement
Used to control execution of set of line, block of code and single line

if expresssion:
    statement1
    statement2

if can use following operators with if conditon
1. Comparision operator
2. identity
3. membership
4. logical operators
"""
"""
User_string=input("Enter your string:  ")
print (User_string)
User_confirmation=input("Do you want to allign text: say yes or no ? ")
if User_confirmation == "yes":
    print(User_string.center(122))
    print(User_string.ljust(122))
    print(User_string.rjust(122))


user_str=input("Enter your string : ")
user_cnf=input("Do you want to conver into lower case: say yes or no ")

if user_cnf == "yes":
    print(user_str.lower())


user_str=input("Enter your string : ")
user_cnf=input("Do you want to conver into lower, upper, title case: say lower, upper or title ")

if user_cnf == "lower":
    print(user_str.lower())
elif user_cnf == "upper":
    print(user_str.upper())
elif user_cnf == "title":
    print(user_str.title())
else:
    print ("user did not provide valid input parameter")
"""

evn_number = [2,4,6,8,10]
user_number=eval(input("enter the your number"))

if user_number in evn_number:
    print (f"{user_number} is present in list")
else:
    print (f"{user_number} not present in list")