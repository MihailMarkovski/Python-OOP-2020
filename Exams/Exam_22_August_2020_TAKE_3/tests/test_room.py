import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room('name', 100, 1)

    def test_init(self):
        self.assertEqual('name', self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(1, self.room.members_count)
        self.assertListEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_raises(self):
        with self.assertRaises(ValueError):
            self.room.expenses = -1