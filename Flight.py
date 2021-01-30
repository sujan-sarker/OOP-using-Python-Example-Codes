class Flight:
    def __init__(self, name, destination, airlines, date):
        self.name = name
        self.destination = destination
        self.airlines = airlines
        self.date = date

    def getInfo(self):
        print(f'Name: {self.name}\n'
              f'Destination: {self.destination}\n'
              f'Airlines: {self.airlines}\n'
              f'Date: {self.date}')


f1 = Flight("sameer","USA", "Singapore","12/1/2021")
print('Flight Information:')
f1.getInfo()
