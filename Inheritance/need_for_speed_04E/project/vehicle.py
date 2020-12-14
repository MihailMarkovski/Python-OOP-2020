class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_to_go = kilometers * self.fuel_consumption
        if fuel_to_go <= self.fuel:
            self.fuel -= fuel_to_go
