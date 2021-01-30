# instance variable
# class variable/static variable

class Student:
    deptName = 'RME'
    stCount = 0
    def __init__(self, name, id):
        self.name = name
        self.id = id
        Student.stCount += 1
    def printInfo(self):
        Student.deptName = 'CSE'
        print(Student.deptName)
    @classmethod
    def classMethod(cls, msg):
        print(msg+' '+cls.deptName )
    @staticmethod
    def staticMethod():
        Student.deptName = 'CSE'
        print(Student.deptName)


st1 = Student('A', 4)

st1.staticMethod()

st1 = Student('B', 5)

st1.staticMethod()

print(Student.deptName)





# instance method
