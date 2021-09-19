import re
text="This is a python and it is easy to learn"
my_patt="is"
print(re.findall(my_patt,text))
print(len(re.findall(my_patt,text)))
match_Pattern=re.findall(my_patt,text)
print(match_Pattern[2])


print(re.findall("i[st]",text))
print(re.findall("p[@y]",text))
print(re.findall("python",text))
print(re.findall("[abcd]",text))
print(re.findall("[a-d]",text))