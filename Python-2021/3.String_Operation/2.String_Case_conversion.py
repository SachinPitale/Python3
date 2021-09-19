#
# Convert the string into lower, upper and title case

Script = "Python Scripting is oops "

print (Script.upper())
print (Script.lower())
print (Script.title())
print (Script.swapcase()) #print first char small for every word and rest of will b capital

print (dir(Script))  #get all the method about string
print(Script.capitalize()) # Print first char of line is always capital
print(Script.replace(" ","-"))
print (Script.casefold()) # all char will  get in lowercase
print (Script.count("i"))  # total number of characther present in string
print(Script.istitle())
print(Script.isspace())
print(Script.find("P")) # Find position of char
print(Script.index("s")) # Find position of char
print (Script.format())
print(Script.endswith("s"))


