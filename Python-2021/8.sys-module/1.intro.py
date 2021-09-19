"""
Introduction of sys module
###############################

The sys module provide functions and variable used to manipulate different parts of the python
runtime environment.

How to use sys module
#########################
import sys

How to get help on sys module
#################################
dir(sys), help(sys)
"""
import sys

print (dir(sys))
#print (help(sys))

print (sys.version)
print (sys.version_info)
print (sys.modules)
sys.exit() ### break the script execution using sys.exit() method, we can provide exit code also by sys.exit(2)
print (sys.path)