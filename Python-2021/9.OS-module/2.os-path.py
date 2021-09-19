"""
os.path is a sub module of os 
os.path module is used to work on paths
Methods
#######################
1. os.path.sep  -> It print the value of path separator
2. os.path.basename(path) -> It will return last value of path either filename or directory name
3. os.path.dirname(path) => It will return the directory path 
4. os.path.join(path1,path2) => It will join the two os path
5. os.path.split(path) => It will split directory path and filename
6. os.path.getsize(path) => It will give output in byte
7. os.path.exists(path) => Check path is exist or not
8. os.path.isdir(path) => It will return the output if last value is directroy
9. os.path.isfile(path) => It will return the output if last value is file.
10. os.path.islink(path) => Check the file is softlink or not
11. os.path.getatime
12. os.path.getctime
13. os.path.getmtime
"""

import os 
print (os.path.sep)
home="G:\\SACHIN\\Practicle\\Python\\Python-2021\\9.OS-module\\2.os-path.py"
print (os.path.basename(home))
print (os.path.dirname(home))

path1="G:\\SACHIN\\Practicle\\Python\\Python-2021"
path2="9.OS-module"

print(os.path.join(path1,path2))
print (os.path.split(home))
print (os.path.getsize(home))
print (os.path.exists(home))

if os.path.exists(path2):
    print ("Path is present")
else:
    print ("path is not present")


print (os.path.isfile(home))
print (os.path.isdir(path1))

if os.path.isfile(path1):
    print (f"{home} is file" ) 
else:
    print (f"{home} is directory")


print (os.path.islink(home))


if os.path.islink(path1):
    print (f"{home} is soft link" ) 
else:
    print (f"{home} not soft link")

