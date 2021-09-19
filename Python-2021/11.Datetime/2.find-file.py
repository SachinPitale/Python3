import os
import sys

req_file=input("Enter your path: ")
if not os.path.exists(req_file):
    print ("{req_file} path is not valid")
    sys.exit()
if os.path.isfile(req_file):
    print ("{req_file} is file")
    sys.exit()

all_objects=os.listdir(req_file)

print(all_objects)

all_files= []
for i in all_objects:
    each_file_path=os.path.join(req_file,i)
    if os.path.isfile(each_file_path):
        print(each_file_path)
    

print (all_files)

