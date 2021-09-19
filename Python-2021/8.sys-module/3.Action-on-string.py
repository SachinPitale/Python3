

#user_string = input("Enter your string:  ")
#user_action = input("Select the string operation like upper,title and lower:  ")
import sys 
user_string = sys.argv[1]
user_action = sys.argv[2]

if user_action == "lower":
    print (user_string.lower())
elif user_action == "upper":
    print (user_string.upper())
elif user_action == "title":
    print (user_string.title())
else:
    print ("Enter valid input paramete only upper,lower,title")