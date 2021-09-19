
def fun(int1,int2):
    sum = int1 + int2
    mul = int1 * int2
    sub = int1 - int2
    div = int1 / int2
    mod = int1 % int2
    return sum, mul, sub, div, mod


print (fun(10,5))
sum, mul, sub, div, mod = fun(10,5)

print (f"sum value is {sum}")
print (f"mul value is {mul}")
print (f"sub value is {sub}")
print (f"div value is {div}")
print (f"mod value is {mod}")