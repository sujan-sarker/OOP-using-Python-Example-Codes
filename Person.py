import datetime


class Person:
    dept = 'RME'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dept = 'CSE'

    def printInfo(self):
        print(self.name, self.age)

    @classmethod
    def classMethod(cls):
        print(cls.dept)

    @classmethod
    def PersonFromYear(cls, name, year):
        return cls(name, datetime.date.today().year - year)

    @staticmethod
    def staticMethod(age):
        return  age >= 18


p1 = Person('ABC', 23)

p2 = Person.PersonFromYear('sujan', 1991)

print(Person.staticMethod(p1.age))
