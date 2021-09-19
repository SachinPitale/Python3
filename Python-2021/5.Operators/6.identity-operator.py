"""
Identity Operators

Identity Operators are used to find the type of class/type/object
There are two types of identity operators
1. is
2. is not

"""
x=5
y='hi'

print (type(x))
print (type(y))

print (type(x) is type(y))
print (type(x) is not type(y))


"""
Membership Operatos
=================================
Membership Operators are used to validate the membership of a value.
They are two types of membership operators:
1. in
2. not in

"""

emp = {
    "sachin" :  "IT",
    "Yogesh" : "Admin",
    "Kunal" : "HR"
}

if "sachin" in emp:
    print ("Hello sachin")


valid_java=['1.6','1.7','1.8','1.9']
install_java='1.6'

if install_java in valid_java:
    print (f"{install_java} version is valid for host")
else:
    print (f"{install_java} version is not valid for host, upgrade your host accordingly")


db_users=['db-admin','sys-admin','admin']
login_user='sachin'

if login_user not in db_users:
    print (f"{login_user} is not authorized to perform the operation")
else:
    print (f"{login_user} authorized to perform the operation")
