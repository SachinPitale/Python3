
num = eval(input("Enter your number: "))
number={
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "Nine",
        10: "ten"

    }
if num in [1,2,3,4,5,6,7,8,9,10]:
    print ("You enter number in 1 to 10 range")
    
    for k,v in number.items():
        if k == num:
            print (f"you enter value is {num} = {v}")
else:
    print ("you enter number is out of range ")


if num in [1,2,3,4,5,6,7,8,9,10]:
    print(number.get(num))
else:
    print ("you enter number is out of range ")