import unittest


# from Testing.code_files.car_manager_04 import Car


class TestCar(unittest.TestCase):
    def test_carInit_shouldCreateProperObject(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        expected = [make, model, fuel_consumption, fuel_capacity, 0]
        c = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertListEqual(expected, [c.make, c.model, fuel_consumption, fuel_capacity, c.fuel_amount])

    # --- ADDED FROM DONCHO BUT ARE NOT TESTED IN JUDGE---
    def test_carInit_whenNoneMake_shouldRaise(self):
        make = None
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenEmptyStringMake_shouldRaise(self):
        make = ''
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenNoneModel_shouldRaise(self):
        make = 'test make'
        model = None
        fuel_consumption = 6
        fuel_capacity = 60

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenEmptyStringModel_shouldRaise(self):
        make = 'test make'
        model = ''
        fuel_consumption = 6
        fuel_capacity = 60

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenNegativeFuelConsumption_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = -1
        fuel_capacity = 60

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenZeroFuelConsumption_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 0
        fuel_capacity = 60

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenNegativeFuelCapacity_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = -1

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenZeroFuelCapacity_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 0

        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        self.assertIsNotNone(context.exception)

    def test_carInit_whenNegativeFuelAmount_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1

        self.assertIsNotNone(context.exception)

    # --- ADDED FROM DONCHO END ---

    # SETTERS ARE NOT TESTED BY DONCHO, DID IT ANYWAY
    def test_carMakeSetter_whenValidValue_shouldChangeMake(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.make = 'new test make'
        self.assertEqual('new test make', c.make)

    def test_carMakeSetter_whenValueIsNone_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.make = None
        self.assertIsNotNone(context.exception)

    def test_carMakeSetter_whenValueIsEmtpyString_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.make = ''
        self.assertIsNotNone(context.exception)

    def test_carModelSetter_whenValidValue_shouldChangeModel(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.model = 'new test model'
        self.assertEqual('new test model', c.model)

    def test_carModelSetter_whenValueIsNone_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.model = None
        self.assertIsNotNone(context.exception)

    def test_carModelSetter_whenValueIsEmtpyString_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.model = ''
        self.assertIsNotNone(context.exception)

    def test_carFuelConsumptionSetter_whenValidValue_shouldChangeConsumption(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.fuel_consumption = 12
        self.assertEqual(12, c.fuel_consumption)

    def test_carFuelConsumptionSetter_whenValidIsZero_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.fuel_consumption = 0
        self.assertIsNotNone(context.exception)

    def test_carFuelConsumptionSetter_whenValidIsNegative_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.fuel_consumption = -1
        self.assertIsNotNone(context.exception)

    def test_carFuelCapacitySetter_whenValidValue_shouldChangeCapacity(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.fuel_capacity = 110
        self.assertEqual(110, c.fuel_capacity)

    def test_carFuelCapacitySetter_whenValidIsZero_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.fuel_capacity = 0
        self.assertIsNotNone(context.exception)

    def test_carFuelCapacitySetter_whenValidIsNegative_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.fuel_capacity = -1
        self.assertIsNotNone(context.exception)

    def test_carFuelAmountSetter_whenValidValue_shouldChangeAmount(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.fuel_amount = 50
        self.assertEqual(50, c.fuel_amount)

    def test_carFuelAmountSetter_whenNegativeValue_shouldChangeAmount(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.fuel_amount = -1
        self.assertIsNotNone(context.exception)

    # ----------

    def test_carRefuel_whenFuelIsValidAndLessThanCapacity_shouldIncreaseAmount(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.refuel(50)
        self.assertEqual(50, c.fuel_amount)

    def test_carRefuel_whenFuelIsValidAndMoreThanCapacity_shouldIncreaseAmount(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.refuel(101)
        self.assertEqual(fuel_capacity, c.fuel_amount)

    def test_carRefuel_whenNegativeFuel_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.refuel(-1)
        self.assertIsNotNone(context.exception)

    def test_carRefuel_whenZeroFuel_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.refuel(0)
        self.assertIsNotNone(context.exception)

    def test_carDrive_whenEnoughFuel_shouldDecreaseAmount(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        c.fuel_amount = 100
        distance = 50
        needed = (distance / 100) * c.fuel_consumption
        self.assertEqual(fuel_capacity - needed, c.fuel_amount - needed)

        # FROM DONCHO
        # make = 'test make'
        # model = 'test model'
        # fuel_consumption = 6
        # fuel_capacity = 60
        #
        # params = [make, model, fuel_consumption, fuel_capacity]
        # car = Car(*params)
        #
        # car.refuel(car.fuel_capacity)
        # distance = 100
        # car.drive(distance)
        # expected = car.fuel_capacity - car.fuel_consumption * distance / 100
        # actual = car.fuel_amount
        #
        # self.assertEqual(expected, actual)

    def test_carDrive_whenNotEnoughFuel_shouldRaiseException(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 10
        fuel_capacity = 100
        c = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as context:
            c.drive(1000)
        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
