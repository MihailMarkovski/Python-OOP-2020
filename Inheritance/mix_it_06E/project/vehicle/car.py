# from Inheritance.mix_it_06E.project.vehicle.vehicle import Vehicle
from project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value <= self.fuel_tank:
            self.__fuel = value
        else:
            self.__fuel = self.fuel_tank

    def drive(self, distance):
        fuel_to_go = self.fuel_consumption * distance
        if fuel_to_go <= self.__fuel:
            self.__fuel -= fuel_to_go
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        try:
            self.get_capacity(self.fuel_tank, self.__fuel + liters)
            self.__fuel += liters
            return self.__fuel
        except Exception as ex:
            return str(ex)
