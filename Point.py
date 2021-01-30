import math
class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def update(self, xo, yo):
        self.move(self.x + xo, self.y + yo)

    def calcDist(self, otherPoint):
        return math.sqrt((self.x-otherPoint.x)**2 + (self.y-otherPoint.y)**2)

    def printPos(self):
        print(f'({self.x}, {self.y})')


p1 = Point(2, 6)
p2 = Point(3, 6)

print(p1.calcDist(p2))
