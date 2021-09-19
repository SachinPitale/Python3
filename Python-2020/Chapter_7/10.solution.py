
name = input("Enter your name :  ")
age = int(input("Enter your age "))
mov = input("Enter your fov movie name :  ").split(",")
songs = input("Enter your fov songs name :  ").split(",")

user_info = {}

user_info['name'] = name
user_info['age'] = age
user_info['mov'] = mov
user_info['songs'] = songs

print (user_info)

for i in user_info.items():
    print (i)