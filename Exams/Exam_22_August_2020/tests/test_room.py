import unittest

from project.appliances.tv import TV
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('name', 1000, 3)

    def test_init(self):
        self.assertEqual('name', self.room.family_name)
        self.assertEqual(1000, self.room.budget)
        self.assertEqual(3, self.room.members_count)
        self.assertEqual(0, len(self.room.children))
        self.assertEqual(0, self.room.expenses)

    def test_expenses_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -25
        self.assertEqual("Expenses cannot be negative", str(ex.exception))
        self.assertIsNotNone(ex.exception)

    def test_expenses_setter(self):
        self.assertEqual(0, self.room.expenses)
        self.room.expenses = 25
        self.assertEqual(25, self.room.expenses)

    def test_calculate_expenses(self):
        self.assertEqual(0, self.room.expenses)
        tv = TV()
        appliances = [tv]
        self.room.calculate_expenses(appliances)
        self.assertEqual(45, self.room.expenses)


if __name__ == '__main__':
    unittest.main()
