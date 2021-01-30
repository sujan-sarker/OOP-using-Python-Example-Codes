class Parent:
    def __init__(self):
        pass

    def anything(self):
        print("Hello from RME DU")


class Child(Parent):

    def __init__(self):
        super().anything()


c1 = Child()


