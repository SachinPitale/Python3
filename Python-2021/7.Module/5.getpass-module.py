
import getpass
#print(help(getpass))
print(dir(getpass))

"""
getpass(): It will accept the user password in secure way
getuser() :  Function display the login name of the user, This function checks the environment variables LOGNAME, USER, LName
and USERNAME, in order and return the value of the first non-empty sring.
"""

#print (getpass.getpass())
print (getpass.getpass(prompt="Enter your db password "))
print (getpass.os)

print (getpass.unix_getpass)
print (getpass.getuser())