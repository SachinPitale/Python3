
import re 
text="it is a python and learnis easy to learn" 








print(re.findall('^i[ts]',text))   # ^ will find first charcter of string
print(re.findall('learn$',text))   # $ will find the last charachter of string
print(re.findall('\\blearn',text))  # find the learn if he has space at left side  
print(re.findall('learn\\b',text))  # find the learn if he has space at left side  
print(re.findall('\\blearn\\b',text))  


print(re.findall('\\n',text)) 