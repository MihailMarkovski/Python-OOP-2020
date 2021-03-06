from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, liters):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_to_go = distance * (self.fuel_consumption + 0.9)
        if fuel_to_go <= self.fuel_quantity:
            self.fuel_quantity -= fuel_to_go

    def refuel(self, liters):
        self.fuel_quantity += liters


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_to_go = distance * (self.fuel_consumption + 1.6)
        if fuel_to_go <= self.fuel_quantity:
            self.fuel_quantity -= fuel_to_go

    def refuel(self, liters):
        self.fuel_quantity += (0.95 * liters)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
