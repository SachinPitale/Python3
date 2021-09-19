"""
Exceptions Examples:
1. Index Error => print(sum[200])
2. Zero Division Error => print (4/0)
3. Import Error  => import fabric
4. Value Error 
5. Type Error => print (4 +'string')
6. Name Error   => print (a)
7. File not found error => fo=open('test1.txt')
8. I/O error

"""


try:
    print ("This is try block")
    #print(4/0)
    print(a)
    #print (4+'str')
    #open('test.txt')
    #name="sachin"
    #print(name[10])
    #import fabric
except ZeroDivisionError:
    print ("Your are division the number by zero")
except NameError:
    print ("Variable is not defined")
except TypeError:
    print ("Type error")
except FileNotFoundError:
    print ("You provided file name doesn't exist")
except IndexError:
    print ("String index is out of range")
except ModuleNotFoundError:
    print ("Module not found")
except Exception as e:
    print (e)
finally:
    print ("Final  exception")