class Person:
    def __init__(self, fname, lname, age):
        self.frist_name = fname
        self.last_name = lname
        self.age = age

    def Full_name(self):
        return f"{self.frist_name}  {self.last_name}"

    def Is_above_18(self):
        if int(self.age) > 18:
            return True
        return False




P1 = Person('sachin','Pitale','29')

print(P1.frist_name)

print (P1.Full_name())
print (P1.Is_above_18())

