"""
What is a Regular Expression(Regex)
########################################
The regex is a procedure in any language to look for a specified pattern in a given text.
What is pattern?
    It is sequence of characters, Which represent multiple strings,
    Ex: 'i[st]' -> is, it
    python[23] -> python2, python3

Regex Operation:
1. match()
2. search()
3. findall()
4. finditer()
5. sub()
6. split()
7. compile()
 
"""

my_str="Python is simple and it easy "
print(my_str.split('is'))

import re
print (re.split("i[st]",my_str))



