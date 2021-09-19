import sys

my_list = [2,5,50,65,8,95]
for i in my_list:
    print (i)
    if i == 65:
        break


path = ['/usr/bin', '/usr/bin/httpd', '/home/users/xyz/weblogic/config.xml']
for i in path:
    if 'httpd' in i:
        print (i)
        break
print ("outside of the for loop")


for i in range(1,11):
    if i == 7:
        continue    
    print(i)


if True:
    pass
    