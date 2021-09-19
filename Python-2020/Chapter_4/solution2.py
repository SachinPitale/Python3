name=input("Enter you name : ")

#def is_palindrom(a):
#
#    new_name = name[::-1]
#    if name == new_name:
#        return "Name is matching"
#    return "name does not match"

def is_palindrom(a):
    return name == name[::-1]


print(is_palindrom(name)) 