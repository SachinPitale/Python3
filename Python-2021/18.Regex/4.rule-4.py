import re

text="This is a pythonnnn and zay zaaaay zaaay python xz  z"















print(re.findall('\\bpython{4}',text)) # It will add 4 times (n)
print(re.findall('\\ba{3}\\b',text))
print(re.findall('\\bza{1,4}y\\b',text)) # it will find the word whose contain a 1 and 4 times
print(re.findall('\\bza{2,}y\\b',text)) 
print(re.findall('\\bza+y\\b',text))  # one or more 
print(re.findall('\\bza*y\\b',text))  # 0 or more times
print(re.findall('\\bza?y\\b',text))                                      # ? once or none(lazy)
