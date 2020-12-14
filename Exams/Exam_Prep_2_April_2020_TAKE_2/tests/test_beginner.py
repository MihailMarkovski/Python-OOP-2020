import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.p = Beginner('test')

    def test_init(self):
        self.assertEqual('test', self.p.username)
        self.assertEqual(50, self.p.health)
        self.assertEqual(0, len(self.p.card_repository.cards))
        self.assertEqual(0, self.p.card_repository.count)

    def test_username_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.p.username = ''
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_username_proper_setter(self):
        self.p.username = 'new'
        self.assertEqual('new', self.p.username)

    def test_health_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.p.health = -3
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_health_proper_setter(self):
        self.p.health = 23
        self.assertEqual(23, self.p.health)

    def test_is_dead(self):
        self.p.health = 100
        self.assertFalse(self.p.is_dead)
        self.p.health = 0
        self.assertTrue(self.p.is_dead)

    def test_take_damage_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.p.take_damage(-23)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

    def test_take_damage(self):
        self.p.take_damage(5)
        self.assertEqual(45, self.p.health)