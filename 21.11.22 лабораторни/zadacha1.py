
class Person:
    def __init__(self, fname, lname, age, nationality):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.nationality = nationality

    def printname(self):
        print(self.firstname, self.nationality)

MyPerson = Person("Yoan", "Ivanov", 45, "Bulgarian")
MyPerson.printname()



class Student(Person):
    def __init__(self, fname, lname, age, nationality, university, yearsofstudy):
        super().__init__(fname, lname, age, nationality)
        self.university=university
        self.yearsofstudy=yearsofstudy

    def printuniversity(self):
        print(self.university, self.yearsofstudy)

MyPerson1 = Student("Yoan", "Ivanov", 45, "Bulgarian", "TU SOFIA", 4)
MyPerson1.printuniversity()

class Lecturer(Person):
    def __init__(self, fname, lname, age, nationality, university, experience):
        super().__init__(fname, lname, age, nationality)
        self.university=university
        self.experience=experience

    def printexperience(self):
        print(self.university, self.experience)

MyPerson2 = Lecturer("Ivan", "Dimitrov", 55, "BUlgarian", "TU Plovdiv", 6)
MyPerson2.printexperience()