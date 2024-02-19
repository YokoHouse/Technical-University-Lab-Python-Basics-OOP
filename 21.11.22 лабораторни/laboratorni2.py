class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

MyPerson = Person('Ivan', 45)

print(MyPerson.name)
print(MyPerson.age)