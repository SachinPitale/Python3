# Basic Addition calculator
# For input parameter we use (input) function in python, but it accept all the input all the input as string
# if you want to enter Integer use int with input (i.e int(input("enter your number: ""))

#Part I
"""
a=input("Enter your first number : ")
b=input("Enter your second number: ")

print (type(a),type(b))



print ("Enter a two number for addition")
Num1=int(input("Enter the first number: "))
Num2=int(input("Enter the Second Number: "))
result=Num1+Num2

print (f"First number is {Num1} and second is {Num2} = total of both the number is {result}")
"""
#Part II
# If you want to check the your variable value at time of input parameter use eval function and pass the string with double quotes.
# i.e eval(input("Enter your first number:"))
"""
Fname=eval(input("Enter your first name: "))
Age=eval(input("Enter your Age: "))

print (f"Your name data type is {Fname}")
print (f"Your age data type is {Age}")
"""
#Part III
"""
Name=eval(input("Enter your full name :  "))
print (Name)
Rname=Name.replace('_','-')
print(Rname)
"""
#
"""
list = [1,2,3,46,78,165,89]
print (list)
print(max(list))
print(min(list))
"""


#

list1 = [10,5,15,25]
list2 = [35,7,10,22]
l1max = (max(list1))
l2max = (max(list2))

if l1max >= l2max:
    print (f"the greater number is from list1 and number is {l1max}")
else:
    print (f"the greater number is from list2 and number is {l2max}")



"""
hig = 0
for i in list1:
    for j in list2:
        if i >= j:
            if hig >= i:
                hig = i
                print (hig)
        else:
            if hig >= j:
                hig = j
"""

    
    
    

        
        