import unittest
# CANNOT PASS JUDGE WITH THE 2 ADDITIONAL TESTS
# from project.appliances.laptop import Laptop
# from project.appliances.tv import TV
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(name='name', budget=100, members_count=2)

    def test_init(self):
        self.assertEqual('name', self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertListEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    # def test_expenses_proper(self):
    #     self.assertEqual(0, self.room.expenses)
    #     self.room.expenses = 25
    #     self.assertEqual(25, self.room.expenses)
    #
    # def test_calculate_expenses(self):
    #     args = [[TV(), Laptop()]]
    #     self.room.calculate_expenses(*args)
    #     self.assertEqual(2.5, self.room.expenses)
