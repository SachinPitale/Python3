"""
How to do a system wide search for a file
"""

import os
import string
import platform

user_search=input("Enter your file or directory, Which you want to search:  ")
user_input=input("This is your file or directory? valid input is file or directory :  ")

if platform.system()=="Windows":

    pd_names=string.ascii_uppercase
    for valid_drive in pd_names:
        if os.path.exists(valid_drive + ":\\"):
            print (valid_drive + ":\\")
            if user_input == "file":
                for r,d,f in os.walk(valid_drive + ":\\"):
                    for each_file in f:
                        if each_file==user_search:
                            print(os.path.join(r,each_file))
            elif user_input == "directory":
                for r,d,f in os.walk(valid_drive + ":\\"):
                    for each_dir in d:
                        if each_dir==user_search:
                            print(os.path.join(r,each_dir))
            else:
                print (f"{user_input} is in valid input parmater, provide only valid directory or file")
else:
    for r,d,f in os.walk("/"):
        if user_input == "file":
            for each_file in f:
                if each_file == user_search:
                    print (os.path.join(r,each_file))
        elif user_input == "directory":
            for each_dir in d:
                if each_dir == user_search:
                    print (os.path.join(r,each_dir)) 
        else:
             print (f"{user_input} is in valid input parmater, provide only valid directory or file")

