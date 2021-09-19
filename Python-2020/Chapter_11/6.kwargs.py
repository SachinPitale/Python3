# kwargs (Keyword arguments)
# **kwargs (dobule star operators)


def func (**kwargs):
    print (kwargs)
    for k, v in kwargs.items():
        print (f"{k} : {v} ")



# func(first_name = 'sachin', last_name = 'pitale')

d = {'name': 'Sachin', 'age' : 29  }
func(**d)