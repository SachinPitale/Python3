import time
import os
import platform
"""
if platform.system() == "window":
    print ("Please wait  for clearing the  screen")
    time.sleep(2)
    os.system("cls")
    print ("Listing the all files and directroy")
    os.system('dir')
else:
    print ("Please wait  for clearing the  screen")
    time.sleep(2)
    os.system("cls")
    print ("Listing the all files and directroy")
    os.system('dir')

"""

def my_word():
    print ("This is python function")




def my_function(cmd1,cmd2):
    print ("Please wait  for clearing the  screen")
    time.sleep(2)
    os.system("cls")
    print ("Listing the all files and directroy")
    os.system('dir')


if platform.system() == "window":
    my_function("cls","dir")
else:
    my_function("clear","ls -lrth")


my_word()
my_word()


