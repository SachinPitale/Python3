import random

winining_number = random.randint(1,100)

number = int(input(" Enter your number between 1 - 100  "))
guess = 1
 
game_over = False
while not game_over:
    if winining_number == number:
        print (f"Your gues correct number, in {guess} time")
        game_over = True  
    else:
        if winining_number < number:
            print ("You guess high number ")
            guess += 1
            number = int(input("Try again"))
        else:
            print ("You guess low number ")
            guess += 1
            number = int(input("Try again"))  

