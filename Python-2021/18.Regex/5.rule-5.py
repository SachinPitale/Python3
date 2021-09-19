import re 




"""
text="this is a string ThIs is a new starting THIs"

print(re.findall("this",text,re.I)) # I is ignore case

"""

text="""  this is a string
this is second line
This is third line
aafsad this
"""

print(re.findall('this',text,re.M)) # only matching character
print(re.findall('this',text,re.M|re.I))
