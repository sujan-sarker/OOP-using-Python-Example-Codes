class VariableTest:
    dept = 'RME'

    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
        self.__pass = 123
    def change(self):
        VariableTest.dept = 'CSE'
    def prtVariable(self):
        print(VariableTest.dept, self.dept)


v1 = VariableTest(2, 'ABC', 'CSE')
print(v1._VariableTest__pass)




