import unittest

# from Testing.code_files.worker_01 import Worker


class WorkerTests(unittest.TestCase):
    def test_workerInit_shouldInitProperly(self):
        name = 'test'
        salary = 100
        energy = 100
        w = Worker(name, salary, energy)
        self.assertListEqual([name, salary, energy], [w.name, w.salary, w.energy])

    def test_workerEnergyIncrementedAfterRest_shouldIncreaseByOne(self):
        name = 'test'
        salary = 100
        energy = 100
        w = Worker(name, salary, energy)
        w.rest()
        self.assertEqual(101, w.energy)

    def test_workerWorkWithZeroEnergy_shouldRaiseException(self):
        name = 'test'
        salary = 100
        energy = 0
        w = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            w.work()
        self.assertIsNotNone(context.exception)

    def test_workerWorkWithNegativeEnergy_shouldRaiseException(self):
        name = 'test'
        salary = 100
        energy = -1
        w = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            w.work()
        self.assertTrue(context.exception)

    def test_workerMoneyIncreaseAfterWork_shouldIncreaseBySalary(self):
        name = 'test'
        salary = 100
        energy = 100
        w = Worker(name, salary, energy)
        w.work()
        self.assertEqual(100, w.money)

    def test_workerEnergyDecreaseAfterWork_shouldIncreaseBySalary(self):
        name = 'test'
        salary = 100
        energy = 100
        w = Worker(name, salary, energy)
        w.work()
        self.assertEqual(99, w.energy)

    def test_workerGetInfo_shouldReturnStringWithCorrectValues(self):
        name = 'test'
        salary = 100
        energy = 100
        w = Worker(name, salary, energy)
        expected = f'{name} has saved {w.money} money.'
        self.assertEqual(expected, w.get_info())


if __name__ == '__main__':
    unittest.main()
