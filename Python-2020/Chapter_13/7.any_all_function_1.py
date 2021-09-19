def my_sum(*args):
    if all ([(type(arg) == int or type(args) == float) for arg in args ]):
        total = 0
        for i in args:
            total += i
        return total
    else:
        return "Wrong number"

print (my_sum(2,4,6,8,10))
print (my_sum(2,4,6,8,10,'hershit'))