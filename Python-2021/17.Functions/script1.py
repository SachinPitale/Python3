
# when we import the script1, it will by default will execute the script first.
# To avoid script1 execution we need use (__name__) variable, bydefult value of variable is __main__ in script1 
# so that it will check the condtion if __name__==__main__, and it will always false, when we call from other script
def add(a,b):
    print (f"addition of {a} and {b} is {a+b}")

def sub(a,b):
    print (f"sub of {a} and {b} is {a-b}")

def main():
    x=10
    y=5
    add(x,y)
    sub(x,y)

if __name__=="__main__":
    main() 


