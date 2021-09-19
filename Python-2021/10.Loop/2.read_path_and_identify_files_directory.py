import os

path=input("Enter your path:  ")

# Script 1
if os.path.exists(path):
    print (f"valid path {path}")
    for r,d,f in os.walk(path):
        for each_file in f:
            print (f"{each_file} is file")
            print ("full path of ", os.path.join(r,each_file))
            
        for each_dir in d:
            print (f"{each_dir} is directory")
            print ("full path of ", os.path.join(r,each_dir))


else:
    print (f"Invalid path {path}")

# Script 2
if os.path.exists(path):
    list=os.listdir(path)
    print (list)
    for i in list:
        object=os.path.join(path,i)
        if os.path.isfile(object):
            print (f" {object} it is file")
        else:
             print (f" {object} it is directory")
       
    

