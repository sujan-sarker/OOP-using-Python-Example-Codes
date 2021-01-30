class Student:
    dept = 'RME'
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.dept = 'EEE'

        #self.sayHello()
        #print(self.dept)

    def sayHello(self):
        print('Hello from RME')
        self.studentInfo()

    def studentInfo(self):
        print(str(self.id) + ' ' + self.name)

s1 = Student(10, 'A')
s2 = Student(10, 'B')
print(s2.__class__.dept)

