import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_init(self):
        card = MagicCard('test')
        self.assertEqual('test', card.name)
        self.assertEqual(5, card.damage_points)
        self.assertEqual(80, card.health_points)

    def test_name_raises(self):
        card = MagicCard('test')
        with self.assertRaises(ValueError) as ex:
            card.name = ''
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_name_setter(self):
        card = MagicCard('test')
        card.name = 'new'
        self.assertEqual('new', card.name)

    def test_damage_raises(self):
        card = MagicCard('test')
        with self.assertRaises(ValueError) as ex:
            card.damage_points = -100
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_damage_setter(self):
        card = MagicCard('test')
        card.damage_points = 15
        self.assertEqual(15, card.damage_points)

    def test_health_raises(self):
        card = MagicCard('test')
        with self.assertRaises(ValueError) as ex:
            card.health_points = -100
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")

    def test_health_setter(self):
        card = MagicCard('test')
        card.health_points = 15
        self.assertEqual(15, card.health_points)
