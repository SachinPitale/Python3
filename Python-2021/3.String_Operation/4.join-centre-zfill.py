
"""
x="python"
print ("*".join(x))
print ("-".join(x))
print("\n".join(x))
print ("\t".join(x))
print (x.center(20))
print(x.zfill(10)) # it will add zero 

y= " Python  "
# Strip function
# It will remove  space from starting and ending side of variable
print(y.strip())

script = "Python scripting is easy Python"
print (script.strip('Python')) # It will remove python from both side
print (script.lstrip('Python')) # It will remove python from left side
print (script.rstrip('Python')) # It will remove python from right side

z="python./i"
print (z.rstrip('./i'))


# Multiple time we can call strip method
Script = "Python scripting is very easy to learn"

print(Script.lstrip('Python').rstrip('learn'))  #Remove Python from left side and learn from right side
"""

# split method
script = "python is easy scripting"
print(script.split()) 

text = " Hello, hi , hi how are you"
print (text.split('hi'))
