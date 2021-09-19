

def func (name,*args, last_name = 'sachin', **kwargs):
    print (name)
    print (last_name)
    print (args)
    print (kwargs)




func ('Python', 1,2,3, a=1, b=2)