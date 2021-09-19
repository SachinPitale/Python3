
"""
What is Module:
###################################
A Module is a file containing python defination and statements. That means module containing pyhon function, classes,
and Variable

# What is use of the module:
#############################
1. Reusability

Note-> If script name is mymodule.py then module name is mymodule

# Types of python module
###############################
1. Default Module
2. Third Party module

# To install new(Third party) module in our environement. use following command.
pip install <module name>
pip install xlwtpip
pip install boto3
pip install paramiko

To list all the python modules 

print (help("modules"))

output
##########################################################################
__future__          _tracemalloc        glob                sched
_abc                _warnings           gzip                secrets
_ast                _weakref            hashlib             select
_asyncio            _weakrefset         heapq               selectors
_bisect             _winapi             hmac                setuptools
_blake2             abc                 html                shelve
_bootlocale         aifc                http                shlex
_bz2                antigravity         math                shutil
##########################################################################

To get to know about the particular module use following command

import math
#print (dir(math))

#Method of math module
print(math.pow(2,5))
print(math.pi)
print (math.remainder)
print (math.factorial(10))


# To know about the each function of any module use following command

import math
print (help(math))
"""
# We can import module two way's
#################################
# 1. import module
#    ex: import math
# 2. from module import *
#    ex: from module import *

# if we use 1st methond, then we will have to call the module function follwing way.
##  import math
#    print (math.pi())
#    print (math.pow(2,3))

# if we use 2nd methond, then we will have to call the module function follwing way.
from math import *
print (pi)
print (pow(2,3))

# To create a the alias of module in your script
import math as m
print (m.pi)

import platform as pt
print (pt.system())

## We can declare multiple module in one line also by comma separated.

import math,os,subprocess,platform,sys
