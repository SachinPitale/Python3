# Script will check user provided path is file or directory 

import os

path=input("Enter your Path: ")
if os.path.exists(path):
    print (f" valid path {path}")
    if os.path.isfile(path):
        print (f"Your enter path is {path} file")
    else:
        print (f"Your enter path is {path} directory")
else:
    print (f"Invalid path {path}")
