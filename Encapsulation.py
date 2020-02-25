class Car:
    def __init__(self, make, model):
        self.make = make
        self.__model = model

    def display(self):
        print(self.make)
        print(self.__model)

    def getModel(self):
        print(self.__model)

    def setModel(self, model):
        self.__model = model

car = Car('BMW', 328)
car.display()
car.setModel(135)
car.getModel()