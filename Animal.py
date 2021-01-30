class Animal(object):
    multicellular = True
    eukaryotic = True

    def __init__(self, name):
        self.name = name
        self.color = 'White'

    def breath(self):
        print(self.color, self.name, 'is breathing')

    def eat(self):
        print(self.color, self.name,  'is eating')

