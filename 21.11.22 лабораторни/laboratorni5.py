class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)

MyPerson=Person('Ivan',"Petrov")
MyPerson.printname()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(self,fname,lname)
        self.graduationyear=2020

MyStudent=Student("Petar", "Vasilev")
MyStudent.printname()
