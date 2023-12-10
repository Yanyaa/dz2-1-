class Human:
    def init(self, name="Human"):
        self.name = name

class Animal:
    def init(self, name="Animal"):
        self.name = name

class Toys:
    def init(self, name="Toys"):
        self.name = name

class Birds:
    def init(self, name="Birds"):
        self.name = name
class Auto1:
    def init(self, brand):
        self.brand = brand
        self.passengers = []

        def add_passenger(self, human):
            self.passengers.append(human) 

        def print_passengers_names(self):
            if self.passengers!= []:
                print(f"Names of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
            else:
                print(f"There are on passengers in {self.brand}")

class Auto2:
    def init(self, brand):
        self.brand = brand
        self.passengers = []

        def add_passenger(self, human):
            self.passengers.append(human) 

        def print_passengers_names(self):
            if self.passengers!= []:
                print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
            else:
                print(f"There are on passengers in {self.brand}")

class Auto3:
    def init(self, brand):
        self.brand = brand
        self.passengers = []

        def add_passenger(self, human):
            self.passengers.append(human) 

        def print_passengers_names(self):
            if self.passengers!= []:
                print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
            else:
                print(f"There are on passengers in {self.brand}")




nick = Human("Nick")
kate = Human("Kate")
tom = Human("Tom")
jane = Human("Jane")
dog = Animal("dog")
bunny = Toys("bunny")
colibri = Birds("colibri")

car1 = Auto1("Mercedes")
car2 = Auto2("Audi")
car3 =Auto3("Schkoda")

car1.add_passenger(nick)
car1.add_passenger(kate)
car2.add_passenger(jane)
car2.add_passenger(tom)
car3.add_animal(dog)
car3.add_toys(bunny)
car3.add_birds(colibri)

car1.print_passengers_names()
car2.print_passengers_names()
