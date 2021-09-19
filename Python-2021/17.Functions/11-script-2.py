#import add, sub function from script1 
# when we import the script1, it will by default will execute the script first.
# To avoid script1 execution we need use (__name__) variable, bydefult value of variable is __main__ in script1 
# so that it will check the condtion if __name__==__main__, and it will always false, when we call from other script

import script1 

def mul(a,b):
    print (f"mul of {a} and {b} is {a*b}")

#print(dir(script1)) #To find out all the function from script1

#print(script1.x)
#print(script1.y)

#call the function
def main():
    x=25
    y=10
    script1.add(x,y)
    #script1.sub(x,y)
    #mul(x,y)


if __name__ == "__main__":
    main()


