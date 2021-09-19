

##Interger Data Type
x=4
y=5.4
z=(5+4j)
"""
Basic Data Type In python
###############################
1. Numbers (int,float and complex)
2. Strings 
3. Boolean
"""



print (x, type(x))
print (y,type(y))
print (z, type(z))


# String Data Type
# String Data type alway's closed with double or single quotes
Lan_name = "Python Scripting"
print (Lan_name)

name = "Sachin"
print (name, type(name))

single_char = "X"
print (single_char, type(single_char))


##Boolen example

my_value=True
my_new_value=False

print (my_value,type(my_value))
print (my_new_value, type(my_new_value))


# Convert Data type into other data type 
"""
1. int,float, complex
2. str
3. bool
"""
# We can not convert String into Number, but we can convert number in string

A=56
print (A, type(A))
B=str(A)
print (B, type(B))


C=35
print (C, type(C))
D=float(C)
print (D, type(D))

E=5.6
print (int(E))


"""
Note: Any Data type can be converted into boolean
      bool(any_data_type)=True or False
      bool(empty)=False
      bool(non-empty)=True
"""
result=bool(0)
print (result)
Fname=""
Name=bool(Fname)
print (Name)
Fname="Sachin"
Name=bool(Fname)
print (Name)
print (bool(None))

num=100
Name=bool(num)
print (num)

