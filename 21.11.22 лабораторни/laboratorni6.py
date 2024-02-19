class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname



class Student(Person):
    def __init__(self, fname, lname,):
        super().__init__(self,fname,lname)
        self.graduationyear=2020

MyStudent = Student("Ivan", "Vazov")
print(MyStudent)