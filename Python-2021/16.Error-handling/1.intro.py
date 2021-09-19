"""
Errors are two types:
syntax erros: no way to handle syntax errors
Runtime Error : Exceptions, There is a way to handle  runtime errors.
How to handle exceptions?
Ans: 
    with try and except block
    try:
        statement -1
        statement -2
        statement -3
    except:
        print ("This is because of something went wrong in the try block")
    
    try:
        statement -1
        statement -2
        statement -3
    except Exception as e:
        print (e)

Exceptions Examples:
1. Index Error => print(sum[200])
2. Zero Division Error
3. Import Error  => import fabric
4. Value Error 
5. Type Error => print (4 +'string')
6. Name Error   => print (a)
7. File not found error => fo=open('test1.txt')
8. I/O error
         
"""

"""
try:
    print (4/0)
except:
    print ("This is error")
"""

"""
try:
    fo=open('test.txt')
    print (fo.read())
    fo.close()
except:
    print ("Error is ")
"""

try:
    fo=open('test1.txt')
    print (fo.read)
    fo.close()
except Exception as e:
    print (e)