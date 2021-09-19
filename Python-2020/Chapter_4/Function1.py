# Print last charater of user name

def last_char(name):
    return name[-1]


name=input("Enter your name : ")
print(last_char(name))

# Print Even or odd number


# def Even_Odd(num):
#     if num%2 == 0:
#         return "Even_number"
#     else:
#         return "Odd_number"

def Even_Odd(num):
    if num%2 == 0:
        return "Even_number"
    return "Odd_number"


num=int(input("Enter your number :  "))
print(Even_Odd(num))



def song():
    return "Happy Birthday to you"


print(song())