import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.c = MagicCard('test')

    def test_init(self):
        self.assertEqual('test', self.c.name)
        self.assertEqual(5, self.c.damage_points)
        self.assertEqual(80, self.c.health_points)

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.c.name = ''
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_name_setter_proper(self):
        self.c.name = 'new'
        self.assertEqual('new', self.c.name)

    def test_damage_points_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.c.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_damage_points_setter_proper(self):
        self.c.damage_points = 123
        self.assertEqual(123, self.c.damage_points)

    def test_health_points_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.c.health_points = -2
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))

    def test_health_points_setter_proper(self):
        self.c.health_points = 123
        self.assertEqual(123, self.c.health_points)
