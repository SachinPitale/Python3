
def even (a):
    return a % 2 == 0


print (even(10))


addition = lambda a : a % 2 == 0

print (addition(15))

last_char = lambda a : a[-1]
print (last_char('Sachin'))


def func (s):
    if len(s) > 5:
        return True
    return False


func = lambda s : True if len(s) > 5 else False
print (func ('sachin'))

func1 = lambda s : len(s) > 13
print (func1 ('sachinPitalelearningpython'))
