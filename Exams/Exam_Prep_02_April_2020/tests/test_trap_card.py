import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_init(self):
        card = TrapCard('test')
        self.assertEqual('test', card.name)
        self.assertEqual(120, card.damage_points)
        self.assertEqual(5, card.health_points)

    def test_name_raises(self):
        card = TrapCard('test')
        with self.assertRaises(ValueError) as ex:
            card.name = ''
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_name_setter(self):
        card = TrapCard('test')
        card.name = 'new'
        self.assertEqual('new', card.name)

    def test_damage_raises(self):
        card = TrapCard('test')
        with self.assertRaises(ValueError) as ex:
            card.damage_points = -100
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_damage_setter(self):
        card = TrapCard('test')
        card.damage_points = 15
        self.assertEqual(15, card.damage_points)

    def test_health_raises(self):
        card = TrapCard('test')
        with self.assertRaises(ValueError) as ex:
            card.health_points = -100
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")

    def test_health_setter(self):
        card = TrapCard('test')
        card.health_points = 15
        self.assertEqual(15, card.health_points)
