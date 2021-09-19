class Person:                                                            # Define a class
    def __init__(self,first_name, last_name, age):
         # init method is similar to construnctor 
        # Instance Variable       # self keyword is represet the object of class, it initialize the instance variable
         print ('init method called ')
         self.first_name = first_name 
         self.last_name = last_name
         self.age = age



p1 = Person('Sachin','pitale', '29' )
p2 = Person('Hershit','raj','24')

print(p1.first_name)

print(p2.first_name)