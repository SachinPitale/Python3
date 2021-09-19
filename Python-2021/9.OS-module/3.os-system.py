"""
os.system()
###########################
It is a function, is used to execute os commands
1. os.getcwd() => Return currnet working directory
2. os.listdir() => Return list of file  and directroy in cwd
"""
import os
import platform
print (os.getcwd())
print (os.listdir())

print (os.system("dir"))
print (os.system("cls"))
#cmd="date"
#print (os.system("cmd"))

print(dir(platform))