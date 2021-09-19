"""
os.walk(path)
########################
Used to generate directory and file names in a directory tree by working
"""

import os 

home="G:\\SACHIN\\Practicle\\Python\\Python-2021\\9.OS-module"
print (os.walk(home))
print (list (os.walk(home)))

for r, d, f in os.walk(home):
    if len(f) != 0:
        print (r) 
        for each_file in f:
            print (os.path.join(r,each_file) )
        print ("-------------------------")
