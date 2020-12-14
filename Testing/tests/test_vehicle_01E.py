import unittest


# from Testing.code_files.vehicle_01E import Car, Truck


class TestCar(unittest.TestCase):
    def test_carInit_shouldCreateProperObject(self):
        fuel_quantity = 100
        fuel_consumption = 10
        car = Car(fuel_quantity, fuel_consumption)
        self.assertListEqual([fuel_quantity, fuel_consumption], [car.fuel_quantity, car.fuel_consumption])

    def test_carDrive_whenEnoughFuel_shouldReduceQuantity(self):
        fuel_quantity = 100
        fuel_consumption = 10
        car = Car(fuel_quantity, fuel_consumption)
        distance = 5
        car.drive(distance)
        fuel_left = fuel_quantity - (distance * (fuel_consumption + 0.9))
        self.assertEqual(fuel_left, car.fuel_quantity)

    def test_carDrive_whenNotEnoughFuel_shouldRemainTheSame(self):
        fuel_quantity = 100
        fuel_consumption = 10
        car = Car(fuel_quantity, fuel_consumption)
        distance = 1000
        car.drive(distance)
        self.assertEqual(fuel_quantity, car.fuel_quantity)

    def test_carRefuel_shouldIncreaseQuantity(self):
        fuel_quantity = 50
        fuel_consumption = 10
        car = Car(fuel_quantity, fuel_consumption)
        car.refuel(50)
        self.assertEqual(100, car.fuel_quantity)


class TestTruck(unittest.TestCase):
    def test_truckInit_shouldCreateProperObject(self):
        fuel_quantity = 100
        fuel_consumption = 10
        truck = Truck(fuel_quantity, fuel_consumption)
        self.assertListEqual([fuel_quantity, fuel_consumption], [truck.fuel_quantity, truck.fuel_consumption])

    def test_truckDrive_whenEnoughFuel_shouldReduceQuantity(self):
        fuel_quantity = 100
        fuel_consumption = 10
        truck = Truck(fuel_quantity, fuel_consumption)
        distance = 5
        truck.drive(distance)
        fuel_left = fuel_quantity - (distance * (fuel_consumption + 1.6))
        self.assertEqual(fuel_left, truck.fuel_quantity)

    def test_truckDrive_whenNotEnoughFuel_shouldRemainTheSame(self):
        fuel_quantity = 100
        fuel_consumption = 10
        truck = Truck(fuel_quantity, fuel_consumption)
        distance = 1000
        truck.drive(distance)
        self.assertEqual(fuel_quantity, truck.fuel_quantity)

    def test_truckRefuel_shouldIncreaseQuantity(self):
        fuel_quantity = 50
        fuel_consumption = 10
        truck = Truck(fuel_quantity, fuel_consumption)
        truck.refuel(50)
        new_total_fuel = fuel_quantity + 50 * 0.95
        self.assertEqual(new_total_fuel, truck.fuel_quantity)


if __name__ == '__main__':
    unittest.main()
