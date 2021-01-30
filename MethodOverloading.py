class data:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x * other.x

data1 = data(5)
data2 = data(6)

print(data1+data2) # data1.__add__(data2)

