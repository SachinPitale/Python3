"""
A String is a sequence of characters. 
In python string is a sequence of unicode charater 
We can't not delete particular character of string
""" 
"""
# String Example

My_Name ='Sachin Pitale'
My_Profession = 'Python Developer'
my_info = """
#I started my career as Linux admin.
#And Move into Automation team.
"""

print (f"My name is {My_Name}, Profession = {My_Profession}.  \nInfo = {my_info}")

"""
"""
## Access The particular Character of string

Scripting = "Python Scripting"
print(Scripting[0])
print(Scripting[-1])
print(Scripting[0:])
print(Scripting[0:12])
print(Scripting[:10])
print(Scripting[:-1])    
"""
"""
# How to find Length of particular string
Scripting = "Python Scripting"

print (len(Scripting))
print (f"length of your variable is : {len(Scripting)}")
"""

# Add two string in one variable
fname = "sachin"
lname = "pitale"

FullName = fname +" " + lname
print (FullName)
