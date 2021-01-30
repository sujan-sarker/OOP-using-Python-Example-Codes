from Animal import Animal


class Herbivorous(Animal, object):

    def eat(self):
        print("I eat only plants.")


class Dog(Animal, object):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def bark(self):
        print(self.color, self.name, 'is barking')

d1 = Dog('Rover', 'Brown')

print(d1.__dict__)

print(issubclass(Dog, object))
print(issubclass(Animal, object))


d1.breath()



