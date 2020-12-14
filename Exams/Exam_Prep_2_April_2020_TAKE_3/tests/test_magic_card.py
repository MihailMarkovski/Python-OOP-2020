import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = MagicCard('test')

    def test_init(self):
        self.assertEqual('test', self.card.name)
        self.assertEqual(5, self.card.damage_points)
        self.assertEqual(80, self.card.health_points)

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