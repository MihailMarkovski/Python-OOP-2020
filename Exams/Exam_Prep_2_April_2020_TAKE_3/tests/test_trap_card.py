import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = TrapCard('test')

    def test_init(self):
        self.assertEqual('test', self.card.name)
        self.assertEqual(120, self.card.damage_points)
        self.assertEqual(5, self.card.health_points)

    def test_name_raises(self):
        with self.assertRaises(ValueError):
            self.card.name = ''

    def test_name_proper(self):
        self.card.name = 'new'
        self.assertEqual('new', self.card.name)

    def test_damage_points_raises(self):
        with self.assertRaises(ValueError):
            self.card.damage_points = -1

    def test_damage_points_proper(self):
        self.card.damage_points = 23
        self.assertEqual(23, self.card.damage_points)

    def test_health_points_raises(self):
        with self.assertRaises(ValueError):
            self.card.health_points = -1

    def test_health_points_proper(self):
        self.card.health_points = 23
        self.assertEqual(23, self.card.health_points)
