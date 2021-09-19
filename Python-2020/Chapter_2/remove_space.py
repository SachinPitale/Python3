# We can remove the space using following method
# lstip() : it will remove all left side space
# rstrip(): It will remove all right side space
# strip() :  It will remove all the spaces

name ="       sachin         " 
print(name)

print(name.lstrip())
print(name.rstrip())
print(name.strip())

# We can replace anything using replace funcation

Name ="Sac        hin"

print(Name)
print(name.replace(" ", ""))

a = input("Enter you name :   ")

print(a)
b=a.replace("_"," " )
print(b.title())
