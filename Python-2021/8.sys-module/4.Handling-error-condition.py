
import sys 

total_argv = len(sys.argv)
print (total_argv)
"""
if total_argv == 3:
    user_string = sys.argv[1]
    user_action = sys.argv[2]

    if user_action == "lower":
        print (user_string.lower())
    elif user_action == "upper":
        print (user_string.upper())
    elif user_action == "title":
        print (user_string.title())
    else:
        print ("Invaild input provided by user")
else:
    print (f"user provided {total_argv} input paramater, script require only three parameter including script name")
"""
if total_argv != 3:
    print (f"user provided {total_argv} input paramater, script require only three parameter including script name")
    sys.exit()

user_string = sys.argv[1]
user_action = sys.argv[2]
if user_action == "lower":
    print (user_string.lower())
elif user_action == "upper":
    print (user_string.upper())
elif user_action == "title":
    print (user_string.title())
else:
    print ("Invaild input provided by user")





